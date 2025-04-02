#!/usr/bin/env python3
"""
批量會議逐字稿總結工具 - 處理整個資料夾的逐字稿 (多線程版本)
"""

import os
import argparse
import time
from pathlib import Path
from src.transcript_summarizer import TranscriptSummarizer
import concurrent.futures
import threading
from datetime import datetime, timedelta

# 添加線程鎖，用於打印輸出，避免多線程打印混亂
print_lock = threading.Lock()

# 添加 API 請求計數器和時間窗口追蹤
api_counter_lock = threading.Lock()
api_requests = []  # 存儲每個 API 請求的時間戳
MAX_REQUESTS_PER_MINUTE = 15  # Gemini API 限制: 15 RPM

def safe_print(*args, **kwargs):
    """線程安全的打印函數"""
    with print_lock:
        print(*args, **kwargs)

def wait_for_api_quota():
    """
    等待 API 配額可用
    確保每分鐘不超過 MAX_REQUESTS_PER_MINUTE 個請求
    """
    current_time = datetime.now()
    
    # 使用鎖來檢查和更新請求計數
    with api_counter_lock:
        # 移除一分鐘前的請求記錄
        one_minute_ago = current_time - timedelta(minutes=1)
        while api_requests and api_requests[0] < one_minute_ago:
            api_requests.pop(0)
        
        # 如果當前一分鐘內的請求數已達到限制，則計算需要等待的時間
        if len(api_requests) >= MAX_REQUESTS_PER_MINUTE:
            oldest_request = api_requests[0]
            wait_time = (oldest_request + timedelta(minutes=1) - current_time).total_seconds()
            if wait_time > 0:
                # 在鎖外等待，避免阻塞其他線程
                safe_print(f"API 請求達到限制，等待 {wait_time:.2f} 秒...")
            else:
                wait_time = 0
        else:
            # 如果未達到限制，記錄新的請求時間並立即返回
            api_requests.append(current_time)
            return True
    
    # 如果需要等待，在鎖外等待
    if wait_time > 0:
        time.sleep(wait_time + 0.5)  # 額外等待 0.5 秒作為緩衝
        # 等待後再次調用自己，重新檢查配額
        return wait_for_api_quota()
    
    # 等待後再次獲取鎖並添加請求
    with api_counter_lock:
        api_requests.append(datetime.now())
        return True

def process_file(file_info):
    """
    處理單個逐字稿文件
    
    Args:
        file_info (tuple): 包含 (file_path, output_dir, output_format, total_files, file_index) 的元組
    
    Returns:
        bool: 處理是否成功
    """
    file_path, output_dir, output_format, total_files, file_index = file_info
    
    # 初始化總結器 (每個線程需要自己的實例)
    summarizer = TranscriptSummarizer()
    
    start_time = time.time()
    safe_print(f"處理 ({file_index+1}/{total_files}): {file_path.name}")
    
    # 讀取逐字稿
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
    except Exception as e:
        safe_print(f"讀取文件 {file_path.name} 時出錯: {e}")
        return False
    
    # 等待 API 配額可用
    try:
        quota_available = wait_for_api_quota()
        if not quota_available:
            safe_print(f"無法獲取 API 配額，跳過處理 {file_path.name}")
            return False
    except Exception as e:
        safe_print(f"等待 API 配額時出錯: {e}")
        # 添加一個簡單的延遲作為備用策略
        time.sleep(10)
    
    # 生成總結
    retry_count = 0
    max_retries = 3
    summary = None
    
    while retry_count < max_retries and summary is None:
        try:
            summary = summarizer.summarize(transcript_text, file_path.name[:-4])
        except Exception as e:
            retry_count += 1
            error_msg = str(e).lower()
            safe_print(f"生成總結時出錯 (嘗試 {retry_count}/{max_retries}): {e}")
            
            # 如果是 API 限制錯誤，等待一段時間後重試
            if any(keyword in error_msg for keyword in ["quota", "rate", "limit", "exceed"]):
                wait_time = 60 * retry_count  # 隨著重試次數增加等待時間
                safe_print(f"檢測到 API 限制錯誤，等待 {wait_time} 秒後重試...")
                time.sleep(wait_time)
                # 重新檢查 API 配額
                try:
                    wait_for_api_quota()
                except:
                    pass  # 即使檢查失敗也繼續嘗試
            elif retry_count < max_retries:
                # 其他錯誤也嘗試重試，但等待時間較短
                time.sleep(5 * retry_count)
            else:
                safe_print(f"達到最大重試次數，放棄處理此文件")
                return False
    
    # 如果所有重試都失敗
    if summary is None:
        safe_print(f"無法為 {file_path.name} 生成總結，跳過")
        return False
    
    # 創建輸出文件名
    output_filename = file_path.stem + f"_summary.{output_format}"
    
    # 為不同格式創建子資料夾
    format_dir = os.path.join(output_dir, output_format)
    with print_lock:  # 使用鎖來確保目錄創建是線程安全的
        os.makedirs(format_dir, exist_ok=True)
    
    # 設定對應格式的輸出路徑
    output_path = os.path.join(format_dir, output_filename)
    
    # 保存總結
    try:
        if output_format == "json":
            summarizer.save_summary(summary, output_path)
        else:
            # 對於txt和md格式，只保存總結文本
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summary["summary"])
            safe_print(f"總結已保存到: {output_path}")
            
            # 為HTML格式創建子資料夾
            html_dir = os.path.join(output_dir, "html")
            with print_lock:  # 使用鎖來確保目錄創建是線程安全的
                os.makedirs(html_dir, exist_ok=True)
            
            # 設定HTML輸出路徑
            html_output_path = os.path.join(html_dir, file_path.stem + "_summary.html")
            # 傳遞文件名作為會議標題
            meeting_title = file_path.stem.replace("_", " ").title()
            summarizer.save_email_html(summary, html_output_path, meeting_title)
            safe_print(f"HTML格式總結已保存到: {html_output_path}")
            end_time = time.time()
            safe_print(f"處理 {file_path.name} 總耗時: {end_time - start_time:.2f} 秒")
    except Exception as e:
        safe_print(f"保存總結 {output_path} 時出錯: {e}")
        return False
    
    return True

def process_directory(input_dir, output_dir, output_format="json", max_workers=4):
    """
    使用多線程處理指定目錄中的所有逐字稿文件
    
    Args:
        input_dir (str): 輸入目錄路徑
        output_dir (str): 輸出目錄路徑
        output_format (str): 輸出格式 (json, txt, md)
        max_workers (int): 最大工作線程數
    """
    # 確保輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 獲取所有文本文件
    file_extensions = ['.txt', '.md', '.text']
    transcript_files = []
    
    for ext in file_extensions:
        transcript_files.extend(list(Path(input_dir).glob(f'*{ext}')))
    
    if not transcript_files:
        print(f"在 {input_dir} 中未找到任何文本文件")
        return
    
    total_files = len(transcript_files)
    
    # 根據 API 限制調整工作線程數
    # 由於 Gemini API 限制為 15 RPM，建議將工作線程數限制在更低值
    adjusted_workers = min(max_workers, MAX_REQUESTS_PER_MINUTE // 4)  # 更保守的設置
    if adjusted_workers < 1:
        adjusted_workers = 1
    
    if adjusted_workers < max_workers:
        print(f"注意: 由於 Gemini API 限制 (15 RPM)，工作線程數已從 {max_workers} 調整為 {adjusted_workers}")
        max_workers = adjusted_workers
    
    print(f"找到 {total_files} 個逐字稿文件，將使用 {max_workers} 個線程並行處理")
    print(f"API 速率限制: 每分鐘 {MAX_REQUESTS_PER_MINUTE} 個請求")
    
    # 準備任務參數
    tasks = [(file_path, output_dir, output_format, total_files, i) 
             for i, file_path in enumerate(transcript_files)]
    
    # 使用線程池執行任務
    start_time = time.time()
    completed = 0
    failed = 0
    
    # 添加進度顯示
    progress_interval = 30  # 每30秒顯示一次進度
    last_progress_time = time.time()
    
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有任務並獲取 future 對象
            futures = {executor.submit(process_file, task): task[0].name for task in tasks}
            
            # 等待所有任務完成
            for future in concurrent.futures.as_completed(futures):
                file_name = futures[future]
                try:
                    if future.result():
                        completed += 1
                    else:
                        failed += 1
                        safe_print(f"處理文件 {file_name} 失敗")
                except Exception as exc:
                    failed += 1
                    safe_print(f"處理文件 {file_name} 時發生異常: {exc}")
                
                # 定期顯示進度
                current_time = time.time()
                if current_time - last_progress_time > progress_interval:
                    elapsed = current_time - start_time
                    progress = (completed + failed) / total_files * 100
                    safe_print(f"進度: {progress:.1f}% ({completed + failed}/{total_files}), "
                              f"已完成: {completed}, 失敗: {failed}, 已用時間: {elapsed:.1f}秒")
                    last_progress_time = current_time
    except KeyboardInterrupt:
        print("\n程序被用戶中斷。正在等待當前任務完成...")
        # 這裡可以添加更多的清理代碼
    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")
    
    end_time = time.time()
    print(f"批量處理完成。成功: {completed}, 失敗: {failed}")
    print(f"總耗時: {end_time - start_time:.2f} 秒")
    print(f"總結文件保存在: {output_dir}")
    
def main():
    parser = argparse.ArgumentParser(description="批量處理會議逐字稿並生成總結 (多線程版本)")
    parser.add_argument("-i", "--input", default="/Users/cfh00896102/Github/gtc2025aiagent/transcript", 
                        help="包含逐字稿文件的輸入目錄 (預設: ./transcript)")
    parser.add_argument("-o", "--output", default="/Users/cfh00896102/Github/gtc2025aiagent/summaries", 
                        help="保存總結的輸出目錄 (預設: ./summaries)")
    parser.add_argument("--format", choices=["json", "txt", "md"], default="md", 
                        help="輸出格式 (預設: md)")
    parser.add_argument("--workers", type=int, default=4, 
                        help="最大工作線程數 (預設: 4)")
    
    args = parser.parse_args()
    
    # 確保輸入目錄存在
    if not os.path.exists(args.input):
        print(f"錯誤: 輸入目錄 {args.input} 不存在")
        return 1
    
    process_directory(args.input, args.output, args.format, args.workers)
    return 0

if __name__ == "__main__":
    exit(main())