import pandas as pd
import random
import markdown
import os
import re
from datetime import datetime

def load_meetings(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")

def select_random_meetings(meetings, categories):
    selected_meetings = {}
    
    for category in categories:
        filtered_meetings = [m for m in meetings if m.get("Topic") == category]
        if filtered_meetings:
            selected_meetings[category] = random.choice(filtered_meetings)
    
    return selected_meetings

def generate_markdown(selected_meetings):
    md_content = """# 開發人員人工智慧大會|NVIDIA GTC 2025  
2025年 3 月 17 ─ 3月21 日  
今年規模比以往更盛大、內容更精彩。數千名開發人員、創新領袖與企業領導者將齊聚一堂，體驗人工智慧和加速運算如何協助人類解決最複雜的挑戰。  
NVIDIA 執行長黃仁勳不容錯過的主題演講，還有超過 1000 場精彩演講、400 多場現場展示、技術實作訓練，以及無數的交流活動，都將讓您探索人工智慧及其優勢的實際案例。  
"""
    
    for category, meeting in selected_meetings.items():
        md_content += f"\n# {category}\n"
        md_content += f"## {meeting.get('Meeting', 'N/A')}\n"
        md_content += f"### {meeting.get('Key', 'N/A')}\n"
    
    return md_content

def markdown_to_email_html(md_content):
    # 轉換 Markdown 為 HTML
    html_content = markdown.markdown(md_content)
    
    # 提取標題和介紹文字，以便後續單獨處理
    title_match = re.search(r'<h1>(.*?)</h1>', html_content)
    title = "開發人員人工智慧大會|NVIDIA GTC 2025"
    if title_match:
        title = title_match.group(1)
    
    # 移除標題和介紹文字，只保留會議內容部分
    # 使用更精確的正則表達式來匹配介紹文字
    intro_pattern = r'<h1>開發人員人工智慧大會\|NVIDIA GTC 2025</h1>.*?<p>2025年 3 月 17 ─ 3月21 日</p>.*?<p>今年規模比以往更盛大.*?</p>.*?<p>NVIDIA 執行長黃仁勳不容錯過的主題演講.*?實際案例。</p>'
    html_content = re.sub(intro_pattern, '', html_content, flags=re.DOTALL)
    
    # 預處理：將連續的 h3 標題分開處理
    html_content = re.sub(
        r'(</h3>)(\s*<h3>)',
        r'\1</div><div class="key-content">\2',
        html_content
    )
    
    # 創建類別到超連結的映射
    category_links = {
        "開發人員人工智慧大會|NVIDIA GTC 2025": "https://www.nvidia.com/zh-tw/gtc/",
        "Keynote": "./topic/GTC 2025 Keynote with nvidia ceo jensen huang_summary.html",
        "Quantum Computing": "./topic/Quantum Computing Where We Are and Where We're Headed [S74495]_summary.html",
        "Business / Executive": "./topic/Business_Executive.html",
        "General Interest": "./topic/General Interest.html",
        "Technical - Beginner": "./topic/Technical - Beginner.html",
        "Technical - Intermediate": "./topic/Technical - Intermediate.html",
        "Technical - Advanced": "./topic/Technical - Advanced.html"
    }
    
    # 處理 h1 標題（類別標題）- 添加超連結
    def add_category_link(match):
        category = match.group(1)
        link = category_links.get(category, f"./topic/{category}.html")
        return f'<div class="category-section"><h1><a href="{link}" class="category-title-link">{category}</a></h1>'
    
    html_content = re.sub(
        r'<h1>(.*?)</h1>',
        add_category_link,
        html_content
    )
    
    # 處理 h2 標題（會議標題）- 添加超連結
    def add_meeting_link(match):
        meeting_title = match.group(1)
        # 創建會議標題的超連結，使用會議名稱作為文件名
        # safe_filename = re.sub(r'[^\w\s-]', '', meeting_title)
        link = f"./topic/session/{meeting_title}_summary.html"
        return f'<div class="meeting-item"><h2><a href="{link}" class="meeting-title-link">{meeting_title}</a></h2>'
    
    html_content = re.sub(
        r'<h2>(.*?)</h2>',
        add_meeting_link,
        html_content
    )
    
    # 處理 h3 標題（會議內容）- 第一個 h3 是描述
    html_content = re.sub(
        r'<h3>(.*?)</h3>',
        r'<h3>\1</h3><div class="key-content">',
        html_content
    )
    
    # 處理列表項目，確保它們在正確的容器內
    html_content = re.sub(
        r'(<ul>.*?</ul>)',
        r'\1</div><div class="key-content">',
        html_content,
        flags=re.DOTALL
    )
    
    # 移除多餘的空 key-content div
    html_content = re.sub(
        r'<div class="key-content"></div>',
        r'',
        html_content
    )
    
    # 清理：移除連續的 div 開始和結束標籤
    html_content = re.sub(
        r'</div>\s*<div class="key-content">',
        r'',
        html_content
    )
    
    # 為每個會議項目添加結束標籤
    # 先找出所有會議項目
    meeting_items = re.findall(r'<div class="meeting-item">.*?(?=<div class="meeting-item">|<div class="category-section">|$)', html_content, re.DOTALL)
    
    # 為每個會議項目添加適當的結束標籤
    for item in meeting_items:
        # 計算 key-content div 的數量
        key_content_count = item.count('<div class="key-content">')
        # 計算已有的結束標籤數量
        end_div_count = item.count('</div>')
        # 需要添加的結束標籤數量
        needed_end_divs = key_content_count + 1 - end_div_count  # +1 是為了 meeting-item div
        
        if needed_end_divs > 0:
            # 創建替換字符串，添加缺少的結束標籤
            replacement = item
            for _ in range(needed_end_divs):
                replacement += '</div>'
            
            # 替換原始字符串
            html_content = html_content.replace(item, replacement)
    
    # 為每個類別添加結束標籤
    category_sections = re.findall(r'<div class="category-section">.*?(?=<div class="category-section">|$)', html_content, re.DOTALL)
    for section in category_sections:
        # 計算開始和結束標籤的數量
        start_tags = section.count('<div')
        end_tags = section.count('</div>')
        
        # 如果結束標籤不足，添加缺少的標籤
        if start_tags > end_tags:
            needed_tags = start_tags - end_tags
            replacement = section
            for _ in range(needed_tags):
                replacement += '</div>'
            
            html_content = html_content.replace(section, replacement)
    
    # 確保所有標籤都正確關閉
    if not html_content.endswith('</div>'):
        html_content += '</div>'
    
    # 當前日期
    current_date = datetime.now().strftime("%Y年%m月%d日")
    
    email_html = f"""
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: 'Roboto', 'Microsoft JhengHei', sans-serif;
                background-color: #f0f2f5;
                color: #333;
                margin: 0;
                padding: 0;
                line-height: 1.6;
            }}
            header {{
                text-align: center;
                padding: 40px 20px;
                background: linear-gradient(135deg, #4b6cb7, #182848);
                color: #fff;
                position: relative;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
                border-radius: 0;
            }}
            header h1 {{
                font-size: 2.4rem;
                margin: 0 0 15px 0;
                letter-spacing: 0.5px;
                text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.3);
            }}
            header p {{
                font-size: 1.2rem;
                margin: 0;
                opacity: 0.9;
            }}
            header img {{
                max-width: 35%;
                height: auto;
                margin-bottom: 20px;
                filter: drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.2));
            }}
            header .date-info {{
                font-size: 1.1rem;
                margin-top: 10px;
                background-color: rgba(255, 255, 255, 0.15);
                display: inline-block;
                padding: 5px 15px;
                border-radius: 20px;
            }}
            main {{
                max-width: 1000px;
                margin: 40px auto;
                padding: 0 20px;
            }}
            .content-container {{
                background-color: #fff;
                border-radius: 12px;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
                padding: 40px;
                margin-bottom: 40px;
            }}
            .section-block {{
                background-color: #fff;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 30px;
                border-left: 5px solid #4b6cb7;
                box-shadow: 0 3px 12px rgba(0, 0, 0, 0.07);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            .section-block:hover {{
                transform: translateY(-5px);
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
            }}
            h1 {{
                color: #2c3e50;
                font-size: 2.1rem;
                margin-top: 0;
                margin-bottom: 30px;
                padding-bottom: 12px;
                border-bottom: 2px solid #4b6cb7;
            }}
            h2 {{
                color: #2980b9;
                font-size: 1.6rem;
                margin-top: 30px;
                margin-bottom: 18px;
                padding-bottom: 10px;
                border-bottom: 1px solid #e0e0e0;
            }}
            h3 {{
                color: #27ae60;
                font-size: 1.3rem;
                margin-top: 25px;
                margin-bottom: 15px;
                font-weight: 600;
            }}
            p {{
                margin-bottom: 18px;
                line-height: 1.8;
                font-size: 1.05rem;
            }}
            ul {{
                padding-left: 20px;
            }}
            li {{
                margin-bottom: 12px;
                position: relative;
                list-style-type: none;
                padding-left: 28px;
                line-height: 1.7;
            }}
            li::before {{
                content: "•";
                position: absolute;
                left: 0;
                color: #4b6cb7;
                font-size: 1.4rem;
                font-weight: bold;
            }}
            footer {{
                text-align: center;
                padding: 35px 20px;
                background-color: #f8f9fa;
                color: #666;
                border-top: 1px solid #e0e0e0;
            }}
            footer img {{
                max-width: 35%;
                height: auto;
                margin-bottom: 20px;
                opacity: 0.9;
            }}
            footer p {{
                margin: 8px 0;
                font-size: 1rem;
            }}
            .category-section {{
                margin-bottom: 60px;
                padding: 30px;
                background-color: #f9f9f9;
                border-radius: 12px;
                border-left: 7px solid #8e44ad;
                box-shadow: 0 5px 18px rgba(0, 0, 0, 0.08);
                transition: transform 0.3s ease;
            }}
            .category-section:hover {{
                transform: translateY(-3px);
            }}
            .category-section h1 {{
                color: #8e44ad;
                font-size: 1.9rem;
                margin-top: 0;
                margin-bottom: 25px;
                padding-bottom: 12px;
                border-bottom: 2px solid #8e44ad;
            }}
            .meeting-item {{
                margin-bottom: 45px;
                padding: 25px;
                background-color: #f7fbff;
                border-radius: 10px;
                border-left: 5px solid #3498db;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }}
            .meeting-item:hover {{
                transform: translateY(-5px);
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            }}
            .meeting-item h2 {{
                color: #3498db;
                font-size: 1.6rem;
                margin-top: 0;
                margin-bottom: 20px;
                padding-bottom: 10px;
                border-bottom: 1px solid #d1e6fa;
            }}
            .key-content {{
                background-color: #f5fffc;
                padding: 20px;
                border-radius: 8px;
                border-left: 4px solid #1abc9c;
                margin-top: 15px;
                margin-bottom: 20px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
            }}
            /* 確保列表項目在 key-content 中正確顯示 */
            .key-content ul {{
                padding-left: 15px;
            }}
            .key-content li {{
                margin-bottom: 10px;
            }}
            .key-content li::before {{
                color: #1abc9c;
            }}
            .intro-text {{
                font-size: 1.15rem;
                line-height: 1.9;
                margin-bottom: 35px;
                padding: 25px;
                background-color: #f0f7ff;
                border-radius: 10px;
                border-left: 5px solid #3498db;
                box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
            }}
            .intro-text p {{
                margin-bottom: 15px;
            }}
            .intro-text p:last-child {{
                margin-bottom: 0;
            }}
            .category-links {{
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                margin: 30px 0;
                justify-content: center;
            }}
            .category-link {{
                display: inline-block;
                padding: 10px 18px;
                background-color: #3498db;
                color: white;
                border-radius: 25px;
                text-decoration: none;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 3px 8px rgba(52, 152, 219, 0.3);
            }}
            .category-link:hover {{
                background-color: #2980b9;
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4);
            }}
            header h1 {{
                color: #FFFFFF;
            }}
            /* 添加響應式設計 */
            @media (max-width: 768px) {{
                header h1 {{
                    font-size: 2rem;
                }}
                .content-container {{
                    padding: 25px;
                }}
                .category-section, .meeting-item {{
                    padding: 20px;
                }}
                .category-links {{
                    gap: 8px;
                }}
                .category-link {{
                    padding: 8px 15px;
                    font-size: 0.9rem;
                }}
            }}
            /* 添加標題超連結樣式 */
            .category-title-link {{
                color: #8e44ad;
                text-decoration: none;
                transition: all 0.3s ease;
            }}
            .category-title-link:hover {{
                color: #9b59b6;
                text-decoration: underline;
            }}
            .meeting-title-link {{
                color: #3498db;
                text-decoration: none;
                transition: all 0.3s ease;
            }}
            .meeting-title-link:hover {{
                color: #2980b9;
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <header>
            <img src="https://i.imgur.com/0LXUWvj.png" alt="GTC 2025 圖示">
            <h1>{title}</h1>
        </header>
        <main>
            <div class="content-container">
                <div class="category-links">
                    <a href="./topic/GTC 2025 Keynote with nvidia ceo jensen huang_summary.html" class="category-link">Keynote</a>
                    <a href="./topic/Quantum Computing Where We Are and Where We're Headed [S74495]_summary.html" class="category-link">Quantum Computing</a>
                    <a href="./topic/Business_Executive.html" class="category-link">Business / Executive</a>
                    <a href="./topic/General Interest.html" class="category-link">General Interest</a>
                    <a href="./topic/Technical - Beginner.html" class="category-link">Technical - Beginner</a>
                    <a href="./topic/Technical - Intermediate.html" class="category-link">Technical - Intermediate</a>
                    <a href="./topic/Technical - Advanced.html" class="category-link">Technical - Advanced</a>
                </div>
                
                {html_content}
            </div>
        </main>
        <footer>
            <img src="https://i.imgur.com/0LXUWvj.png" alt="GTC 2025 圖示">
            <p>此摘要由 AI 輔助生成</p>
            <p>如有任何問題或需要更多詳細資訊，請聯繫 ITR 小組</p>
        </footer>
    </body>
    </html>
    """
    return email_html

def ensure_directories():
    os.makedirs("../report/md", exist_ok=True)
    os.makedirs("../report/topic", exist_ok=True)

def main():
    file_path = "../研討會會議清單.xlsx"  # 修改為你的 Excel 檔案路徑
    categories = [
        "Keynote", "Quantum Computing", "Business / Executive", "Technical - Beginner", 
        "General Interest", "Technical - Intermediate", "Technical - Advanced"
    ]
    
    ensure_directories()
    
    meetings = load_meetings(file_path)
    selected_meetings = select_random_meetings(meetings, categories)
    markdown_output = generate_markdown(selected_meetings)
    html_output = markdown_to_email_html(markdown_output)
    
    # 保存 Markdown 文件
    with open("../report/md/homepage.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_output)
    
    # 保存 HTML 文件
    with open("../report/homepage.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_output)
    
    print("首頁 Markdown 和 HTML 文件已成功生成。")

if __name__ == "__main__":
    main()
