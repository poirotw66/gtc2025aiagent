#!/usr/bin/env python3
"""
批量會議逐字稿總結工具 - 處理整個資料夾的逐字稿
"""

import os
import argparse
import time
from pathlib import Path
from src.transcript_summarizer import TranscriptSummarizer
import time

def process_directory(input_dir, output_dir, output_format="json", delay=1):
    """
    處理指定目錄中的所有逐字稿文件
    
    Args:
        input_dir (str): 輸入目錄路徑
        output_dir (str): 輸出目錄路徑
        output_format (str): 輸出格式 (json, txt, md)
        delay (int): 每次API請求之間的延遲秒數，避免超過API限制
    """
    # 確保輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 初始化總結器
    summarizer = TranscriptSummarizer()
    
    # 獲取所有文本文件
    file_extensions = ['.txt', '.md', '.text']
    transcript_files = []
    
    for ext in file_extensions:
        transcript_files.extend(list(Path(input_dir).glob(f'*{ext}')))
    
    if not transcript_files:
        print(f"在 {input_dir} 中未找到任何文本文件")
        return
    
    print(f"找到 {len(transcript_files)} 個逐字稿文件")
    
    # 處理每個文件
    for i, file_path in enumerate(transcript_files):
        start_time = time.time()
        print(f"處理 ({i+1}/{len(transcript_files)}): {file_path.name}")
        
        # 讀取逐字稿
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                transcript_text = f.read()
        except Exception as e:
            print(f"讀取文件 {file_path.name} 時出錯: {e}")
            continue
        
        # 生成總結
        summary = summarizer.summarize(transcript_text, file_path.name[:-4])
        
        # 創建輸出文件名
        output_filename = file_path.stem + f"_summary.{output_format}"
        
        # 為不同格式創建子資料夾
        format_dir = os.path.join(output_dir, output_format)
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
                print(f"總結已保存到: {output_path}")
                
                # 為HTML格式創建子資料夾
                html_dir = os.path.join(output_dir, "html")
                os.makedirs(html_dir, exist_ok=True)
                
                # 設定HTML輸出路徑
                html_output_path = os.path.join(html_dir, file_path.stem + "_summary.html")
                # 傳遞文件名作為會議標題
                meeting_title = file_path.stem.replace("_", " ").title()
                summarizer.save_email_html(summary, html_output_path, meeting_title)
                print(f"HTML格式總結已保存到: {html_output_path}")
                end_time = time.time()
                print(f"總耗時: {end_time - start_time:.2f} 秒")
        except Exception as e:
            print(f"保存總結 {output_path} 時出錯: {e}")
        
        # 添加延遲以避免超過API限制
        if i < len(transcript_files) - 1:
            time.sleep(delay)
    
    print(f"批量處理完成。總結文件保存在: {output_dir}")
    
    

def main():
    parser = argparse.ArgumentParser(description="批量處理會議逐字稿並生成總結")
    parser.add_argument("-i", "--input", default="/Users/cfh00896102/Github/gtc2025aiagent/transcript", 
                        help="包含逐字稿文件的輸入目錄 (預設: ./transcript)")
    parser.add_argument("-o", "--output", default="/Users/cfh00896102/Github/gtc2025aiagent/summaries", 
                        help="保存總結的輸出目錄 (預設: ./summaries)")
    parser.add_argument("--format", choices=["json", "txt", "md"], default="md", 
                        help="輸出格式 (預設: md)")
    parser.add_argument("--delay", type=int, default=1, 
                        help="每次API請求之間的延遲秒數 (預設: 1)")
    
    args = parser.parse_args()
    
    # 確保輸入目錄存在
    if not os.path.exists(args.input):
        print(f"錯誤: 輸入目錄 {args.input} 不存在")
        return 1
    
    process_directory(args.input, args.output, args.format, args.delay)
    return 0

if __name__ == "__main__":
    exit(main())