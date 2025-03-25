#!/usr/bin/env python3
"""
會議逐字稿總結工具 - 命令行介面
"""

import argparse
import os
from src.transcript_summarizer import TranscriptSummarizer

def main():
    parser = argparse.ArgumentParser(description="使用Gemini 2.0 API總結會議逐字稿")
    parser.add_argument("input_file", help="逐字稿文件路徑")
    parser.add_argument("-o", "--output", help="輸出文件路徑", default="meeting_summary.json")
    parser.add_argument("--format", choices=["json", "txt", "md"], default="json", 
                        help="輸出格式 (預設: json)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"錯誤: 找不到文件 {args.input_file}")
        return 1
    
    # 讀取逐字稿
    with open(args.input_file, 'r', encoding='utf-8') as f:
        transcript_text = f.read()
    
    # 初始化總結器並生成總結
    summarizer = TranscriptSummarizer()
    summary = summarizer.summarize(transcript_text)
    
    # 根據格式保存輸出
    output_path = args.output
    if args.format == "json":
        summarizer.save_summary(summary, output_path)
    else:
        # 對於txt和md格式，只保存總結文本
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(summary["summary"])
        print(f"總結已保存到: {output_path}")
    
    return 0

if __name__ == "__main__":
    exit(main())