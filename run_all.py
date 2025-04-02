#!/usr/bin/env python3
"""
GTC 2025 AI Agent 批次處理排程腳本
此腳本按順序執行所有必要的處理步驟，包括：
1. 處理會議逐字稿
2. 處理主題演講逐字稿
3. 生成會議報告
4. 生成首頁
"""

import os
import subprocess
import time
import argparse
from datetime import datetime

def run_command(command, description):
    """執行命令並顯示進度"""
    print(f"\n{'='*80}")
    print(f"執行: {description}")
    print(f"命令: {command}")
    print(f"開始時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print('-'*80)
    
    start_time = time.time()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    end_time = time.time()
    
    print(f"完成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"耗時: {end_time - start_time:.2f} 秒")
    
    if result.returncode == 0:
        print("狀態: 成功")
        print(f"輸出:\n{result.stdout[:500]}...")  # 只顯示前500個字符
    else:
        print("狀態: 失敗")
        print(f"錯誤:\n{result.stderr}")
    
    return result.returncode == 0

def main():
    parser = argparse.ArgumentParser(description="執行 GTC 2025 AI Agent 的所有處理步驟")
    parser.add_argument("--transcript-dir", default="./data/transcript/", 
                        help="會議逐字稿目錄 (預設: ./data/transcript/)")
    parser.add_argument("--keynote-dir", default="./data/keynote/", 
                        help="主題演講逐字稿目錄 (預設: ./data/keynote/)")
    parser.add_argument("--excel-file", default="./研討會會議清單.xlsx", 
                        help="會議清單 Excel 文件 (預設: ./研討會會議清單.xlsx)")
    parser.add_argument("--output-dir", default="./report/", 
                        help="輸出目錄 (預設: ./report/)")
    parser.add_argument("--topic-dir", default="./report/topic/", 
                        help="主題輸出目錄 (預設: ./report/topic/)")
    
    args = parser.parse_args()
    
    # 確保輸出目錄存在
    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.topic_dir, exist_ok=True)
    
    # 記錄開始時間
    overall_start = time.time()
    print(f"開始執行全部處理步驟: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 步驟 1: 處理會議逐字稿
    success = run_command(
        f"python batch_summarize_process.py -i \"{args.transcript_dir}\" -o \"{args.topic_dir}\"",
        "處理會議逐字稿"
    )
    if not success:
        print("警告: 處理會議逐字稿時出現錯誤，但將繼續執行後續步驟")
    
    # 步驟 2: 處理主題演講逐字稿
    success = run_command(
        f"python batch_summarize_process.py -i \"{args.keynote_dir}\" -o \"{args.topic_dir}\"",
        "處理主題演講逐字稿"
    )
    if not success:
        print("警告: 處理主題演講逐字稿時出現錯誤，但將繼續執行後續步驟")
    
    # 步驟 3: 生成會議報告
    success = run_command(
        f"python src/generate_meeting_report.py -i \"{args.excel_file}\" -o \"{args.topic_dir}\"",
        "生成會議報告"
    )
    if not success:
        print("警告: 生成會議報告時出現錯誤，但將繼續執行後續步驟")
    
    # 步驟 4: 生成首頁
    success = run_command(
        f"python src/generate_homepage.py -i \"{args.excel_file}\" -o \"{args.output_dir}\"",
        "生成首頁"
    )
    if not success:
        print("警告: 生成首頁時出現錯誤")
    
    # 記錄結束時間
    overall_end = time.time()
    print(f"\n{'='*80}")
    print(f"全部處理步驟完成")
    print(f"總耗時: {overall_end - overall_start:.2f} 秒")
    print(f"結束時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"輸出目錄: {args.output_dir}")
    print(f"主題目錄: {args.topic_dir}")

if __name__ == "__main__":
    main()