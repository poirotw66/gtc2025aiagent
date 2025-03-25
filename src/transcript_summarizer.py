"""
會議逐字稿總結工具 - 使用Gemini 2.0 API
"""

import os
import sys
import json
import google.generativeai as genai
from pathlib import Path

# 添加專案根目錄到系統路徑
sys.path.append(str(Path(__file__).parent.parent))

from config.config import GEMINI_API_KEY, MAX_TRANSCRIPT_LENGTH

class TranscriptSummarizer:
    """使用Gemini 2.0 API總結會議逐字稿的類"""
    
    def __init__(self):
        """初始化Gemini客戶端"""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def summarize(self, transcript_text):
        """
        總結會議逐字稿
        
        Args:
            transcript_text (str): 會議逐字稿文本
            
        Returns:
            dict: 包含總結內容的字典
        """
        if len(transcript_text) > MAX_TRANSCRIPT_LENGTH:
            print(f"警告: 文本長度超過{MAX_TRANSCRIPT_LENGTH}字符，可能需要分段處理")
        
        prompt = f"""
        請分析以下會議逐字稿並提供詳細總結，輸出必須為繁體中文，並以會議名稱作為標題。總結應包含以下結構化內容：
        1.研討會主題與目標:簡要說明會議的技術重點，例如探討的新技術、框架或最佳實踐。
        2.主要技術討論點:涵蓋關鍵技術概念、問題分析、最佳實踐、性能優化、實施細節等。
        3.決策與共識:參與者對技術選型、架構決策、方案優劣分析等方面的共識或決策。
        4.時間規劃與里程碑:設定的階段性目標、里程碑、截止日期等。
        5.未解決的技術挑戰:會議中仍未解決的技術問題，可能的解決方向或待進一步研究的內容。
        6.後續行動計劃:下一步應執行的具體技術工作，例如 PoC（概念驗證）、原型開發、測試、技術文檔撰寫等。

        請直接輸出整理後的總結內容，避免多餘的解釋或非必要的輸出。
        
        會議逐字稿:
        {transcript_text}
        """
        
        try:
            response = self.model.generate_content(prompt)
            return {
                "summary": response.text,
                "status": "success"
            }
        except Exception as e:
            return {
                "summary": "",
                "status": "error",
                "error_message": str(e)
            }
    
    def save_summary(self, summary, output_path):
        """
        保存總結到文件
        
        Args:
            summary (dict): 總結內容
            output_path (str): 輸出文件路徑
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        print(f"總結已保存到: {output_path}")
    
    def generate_email_html(self, summary_text, meeting_title=None):
        """
        將會議摘要轉換為 Email HTML 格式
        
        Args:
            summary_text (str): 會議摘要文本
            meeting_title (str, optional): 會議標題，如果為 None 則嘗試從摘要中提取
            
        Returns:
            str: HTML 格式的會議摘要
        """
        # 如果沒有提供會議標題，嘗試從摘要的第一行提取
        if meeting_title is None:
            lines = summary_text.strip().split('\n')
            if lines:
                meeting_title = lines[0].strip('# ').strip()
            else:
                meeting_title = "會議摘要"
        
        # 當前日期
        from datetime import datetime
        current_date = datetime.now().strftime("%Y年%m月%d日")
        
        # 將 Markdown 格式轉換為 HTML
        try:
            import markdown
            html_content = markdown.markdown(summary_text)
        except ImportError:
            # 如果 markdown 模組不可用，進行簡單的轉換
            html_content = summary_text.replace('\n', '<br>')
            html_content = html_content.replace('# ', '<h1>')
            html_content = html_content.replace('## ', '<h2>')
            html_content = html_content.replace('### ', '<h3>')
        
        # 創建 Email HTML 模板
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>{meeting_title}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background-color: #f5f5f5;
                    padding: 15px;
                    border-bottom: 2px solid #ddd;
                    margin-bottom: 20px;
                }}
                .footer {{
                    margin-top: 30px;
                    padding-top: 10px;
                    border-top: 1px solid #ddd;
                    font-size: 0.9em;
                    color: #777;
                }}
                h1 {{
                    color: #2c3e50;
                }}
                h2 {{
                    color: #3498db;
                    border-bottom: 1px solid #eee;
                    padding-bottom: 5px;
                }}
                h3 {{
                    color: #2980b9;
                }}
                ul, ol {{
                    padding-left: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>{meeting_title}</h1>
                <p>日期: {current_date}</p>
            </div>
            
            <div class="content">
                {html_content}
            </div>
            
            <div class="footer">
                <p>此摘要由 AI 輔助生成，如有任何問題或需要更多詳細資訊，請聯繫會議組織者。</p>
            </div>
        </body>
        </html>
        """
        
        return html_template
    
    def save_email_html(self, summary, output_path):
        """
        將會議摘要保存為 Email HTML 文件
        
        Args:
            summary (dict): 包含摘要內容的字典
            output_path (str): 輸出文件路徑
        """
        if summary["status"] != "success":
            print(f"錯誤: 無法生成 Email HTML，摘要生成失敗")
            return
        
        html_content = self.generate_email_html(summary["summary"])
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Email HTML 已保存到: {output_path}")


if __name__ == "__main__":
    # 簡單的命令行介面
    if len(sys.argv) < 2:
        print("用法: python transcript_summarizer.py <逐字稿文件路徑> [輸出文件路徑]")
        sys.exit(1)
    
    transcript_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "meeting_summary.json"
    
    if not os.path.exists(transcript_path):
        print(f"錯誤: 找不到文件 {transcript_path}")
        sys.exit(1)
    
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript_text = f.read()
    
    summarizer = TranscriptSummarizer()
    summary = summarizer.summarize(transcript_text)
    
    # 保存 JSON 格式摘要
    summarizer.save_summary(summary, output_path)
    
    # 同時保存 HTML 格式摘要
    html_output_path = output_path.rsplit('.', 1)[0] + '.html'
    summarizer.save_email_html(summary, html_output_path)