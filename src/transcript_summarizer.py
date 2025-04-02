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
from src.meeting_list_reader import meeting_list

class TranscriptSummarizer:
    """使用Gemini 2.0 API總結會議逐字稿的類"""
    
    def __init__(self):
        """初始化Gemini客戶端"""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        # self.model = genai.GenerativeModel('gemini-2.0-flash-lite')
        # self.model = genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    
    def summarize(self, transcript_text, meeting_title):
        """
        總結會議逐字稿
        
        Args:
            transcript_text (str): 會議逐字稿文本
            
        Returns:
            dict: 包含總結內容的字典
        """
        if len(transcript_text) > MAX_TRANSCRIPT_LENGTH:
            print(f"警告: 文本長度超過{MAX_TRANSCRIPT_LENGTH}字符，可能需要分段處理")
        url = meeting_list.get_url_by_meeting_name(meeting_title)
        prompt = f"""
        請遵循以下步驟處理提供的會議逐字稿：

        1.  內部校對：
            *   仔細閱讀下方提供的「會議逐字稿」。
            *   在內部處理中，找出並修正逐字稿裡最明顯的錯字或口誤（例如：同音異字、打字錯誤、常見用詞錯誤）。
            *   使用建議的正確詞彙替換錯誤詞彙。
            *   將簡體中文翻譯成繁體中文。
            *   重要限制：校正時必須保持句子原有語氣，忠於原文意涵，僅修正明顯錯誤，避免過度詮釋或修改。
            *   此校對結果不需輸出。

        2.  產生會議總結：
            *   基於內部校對後的逐字稿內容，撰寫一份詳細的會議總結。
            *   總結的標題應為下方提供的「會議名稱」，輸出原文然後下方附上會議url,url標題是"會議影片連結"(參考範例),第二行輸出繁體中文翻譯,不用印出"會議名稱:"等字。
            *   總結內容必須包含以下結構化段落，並使用提供的段落標題：
                *   Key Takeaways: 包含概述本會議、重點摘要、Topic（參考範例）。
                *   會議主題: 簡述會議的技術重點（如：探討的新技術、框架、最佳實踐）。
                *   主要技術點: 涵蓋關鍵技術概念、問題分析、最佳實踐、性能優化、實施細節等。
                *   決策與共識: 記錄參與者們在技術選型、架構、方案優劣分析等方面的共識或決策。
                *   時間規劃與里程碑: 列出設定的階段性目標、里程碑、截止日期等。
                *   未解決的技術挑戰: 說明會議中未能解決的技術問題，可能的解決方向或待研究內容。
                *   後續行動計劃: 列出下一步應執行的具體技術工作（如：PoC、原型開發、測試、文檔撰寫）。

        3.  輸出要求：
            *   最終輸出內容僅包含步驟 2所述的會議總結。
            *   請勿輸出校對過程、校對後的逐字稿、或任何非總結內容的額外說明文字。
            *   輸出格式必須為 Markdown。
            *   輸出語言必須為繁體中文。
            *   總結的段落之間要有明確的分隔。
        會議逐字稿:
        {transcript_text}

        會議名稱:
        {meeting_title}

        會議url:
        {url}

        輸出範例:
            # 次世代技術によるリアルタイムAI分析プラットフォームの社会実装に向けて [S71773]
            [會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E6%AC%A1%E4%B8%96%E4%BB%A3%E6%8A%80%E8%A1%93%E3%81%AB%E3%82%88%E3%82%8B%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0AI%E5%88%86%E6%9E%90%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%81%AE%E7%A4%BE%E4%BC%9A%E5%AE%9F%E8%A3%85%E3%81%AB%E5%90%91%E3%81%91%E3%81%A6&tab.catalogallsessionstab=16566177511100015Kus#/session/1726122075292001omB6)
            # 次世代技術實現即時AI分析平台的社會應用 [S71773]

            ## Key Takeaways
            本文將介紹我們在2025年大阪萬博NTT展館中，支援各種應用情境的即時AI分析平台專案。我們將分享專案的歷程、重要的技術進展、心得以及未來的發展方向。我們的平台利用IOWN（創新光無線網路），採用最先進的地理分散式基礎設施技術，驗證其在延遲、擴展性和能源效率方面的有效性。
            ### 重點摘要：
            * 2025年大阪萬博NTT展館展出的AI應用案例。例如：根據參觀者的表情控制牆壁的移動、偵測參觀者跌倒並立即救援、以及為保護隱私而進行模糊處理。
            * 基於IOWN APN（全光網絡）和RDMA（遠端直接記憶體存取），採用地理上三層分散的處理模型（客戶端邊緣、邊緣雲和公有雲）的AI分析平台概述。
            * 充分利用nvJPEG、CV-CUDA、Rivermax和GPUDirect RDMA等先進的卸載技術，打造用於AI推論的高速數據管道。
            * 利用Kubernetes和CDI（可組合分解式基礎架構）對高速數據管道進行擴展，優化硬體資源利用率，大幅降低能源消耗。通過RDMA基於的數據管道串聯，支援將多個AI模型的結果結合起來，實現附加價值更高的複雜AI應用情境。
            ### Topic: 
            * AI Platforms
            * Deployment - AI Inference
            * Inference Microservices

            ## 會議主題
            會議主要探討了如何利用 NTT 的 ION 技術，特別是 DCI（Data Centric Infrastructure）架構和 APN（All-Photonics Network）網路，構建一個低功耗、高效能、即時的 AI 分析平台，並將其應用於大阪萬博的相關服務中。

            ## 主要技術點
            *   **DCI 架構：** 以數據為中心，將計算資源細分，僅啟動必要的計算資源，實現高效能和低功耗。
            *   **APN 網路：** 利用光纖技術實現端到端的直接高速通信，提供大容量和低延遲的連接。
            *   **RDMA 通訊：** 在 GPU 記憶體之間直接通信，減少 CPU 的參與，降低功耗並提高 GPU 的使用效率。
            *   **事件驅動型 AI 推論處理：** 將影像串流處理和 AI 推論處理分離，根據先前的推論結果控制處理流程，在無人時使用輕量級的物件檢測，有人時提供完整的 AI 分析服務。
            *   **硬體加速器卸載：** 利用 SmartNIC 等硬體加速器的功能，將各種處理卸載到硬體上，實現高效能和低功耗。
            *   **CDI（Composable Disaggregated Infrastructure）：** 透過 CDI 伺服器和 DCI 控制器，實現計算資源的靈活組合和分配，根據應用程式的特性進行最佳化。
            *   **AI 隱私遮罩技術：** 使用 NTT 數據的 AI 隱私遮罩技術，模糊人臉，保護隱私。

            ## 決策與共識
            *   採用 DCI 架構和 APN 網路，以實現低功耗、高效能和即時的 AI 分析平台。
            *   利用 RDMA 通訊和硬體加速器卸載，提高 GPU 的使用效率並降低功耗。
            *   採用事件驅動型 AI 推論處理，根據實際情況調整處理流程，實現資源的最佳化利用。
            *   在大阪萬博的相關服務中應用 DCI 技術，包括混雜判定、跌倒檢測和熱度分析。

            ## 時間規劃與里程碑
            *   2026 年實現 DCI 的商業化。
            *   在大阪萬博（2025 年）中展示 DCI 技術的應用。
            *   持續進行研究開發，以進一步提高 DCI 的效能和效率。

            ## 未解決的技術挑戰
            *   硬體切換時間過長，目前只能根據白天或夜晚進行粗略的資源調整。
            *   需要進一步開發短時間切換的技術，以實現更精細的資源管理。

            ## 後續行動計劃
            *   繼續開發 DCI2，目標是實現 8 倍的電力效率提升。
            *   在大阪萬博中實際部署和運行 DCI 系統，收集數據並進行優化。
            *   進一步研究和開發硬體切換技術，以實現更快速和靈活的資源調整。
            *   將 DCI 技術應用於更多領域，推動 AI 系統的社會應用。

        """
        
        try:
            generation_config = genai.GenerationConfig(temperature=0.1)
            # response = self.model.generate_content(contents=prompt)
            response = self.model.generate_content(contents=prompt, generation_config=generation_config)
            summary_text = response.text
            
            # 提取 Key Takeaways 部分
            key_takeaways = self._extract_key_takeaways(summary_text)
            
            # 將 Key Takeaways 存入 Excel 檔案
            self._save_key_takeaways_to_excel(meeting_title, key_takeaways)
            
            return {
                "summary": summary_text,
                "status": "success",
                "key_takeaways": key_takeaways
            }
        except Exception as e:
            return {
                "summary": "",
                "status": "error",
                "error_message": str(e)
            }
    
    def _extract_key_takeaways(self, summary_text):
        """
        從摘要文本中提取 Key Takeaways 部分
        
        Args:
            summary_text (str): 摘要文本
            
        Returns:
            str: Key Takeaways 內容
        """
        lines = summary_text.strip().split('\n')
        key_takeaways = ""
        in_key_takeaways = False
        
        for i, line in enumerate(lines):
            if line.startswith('## Key Takeaways'):
                in_key_takeaways = True
                continue
            
            if in_key_takeaways:
                # 如果遇到下一個段落標題，結束提取
                if line.startswith('## ') and not line.startswith('## Key Takeaways'):
                    break
                key_takeaways += line + '\n'
        
        return key_takeaways.strip()
    
    def _save_key_takeaways_to_excel(self, meeting_title, key_takeaways):
        """
        將 Key Takeaways 存入 Excel 檔案
        
        Args:
            meeting_title (str): 會議標題
            key_takeaways (str): Key Takeaways 內容
        """
        try:
            import pandas as pd
            from pathlib import Path
            
            # Excel 檔案路徑
            excel_path = Path.home() / "Github" / "gtc2025aiagent" / "研討會會議清單.xlsx"
            
            # 檢查檔案是否存在
            if not excel_path.exists():
                print(f"警告: 找不到 Excel 檔案 {excel_path}")
                return
            
            # 讀取 Excel 檔案
            df = pd.read_excel(excel_path)
            
            # 檢查是否有 'Meeting' 欄位
            if 'Meeting' not in df.columns:
                print("警告: Excel 檔案中沒有 'Meeting' 欄位")
                return
            
            # 檢查是否有 'Key' 欄位，如果沒有則新增
            if 'Key' not in df.columns:
                df['Key'] = ""
            
            # 尋找對應的會議標題並更新 Key 欄位
            found = False
            for i, row in df.iterrows():
                if str(row['Meeting']) == meeting_title:
                    df.at[i, 'Key'] = key_takeaways
                    found = True
                    break
            
            if not found:
                print(f"警告: 在 Excel 檔案中找不到會議標題 '{meeting_title}'")
                return
            
            # 保存 Excel 檔案
            df.to_excel(excel_path, index=False)
            print(meeting_title)
            print(f"已將 Key Takeaways 存入 Excel 檔案: {excel_path}")
            
        except Exception as e:
            print(f"存入 Excel 檔案時發生錯誤: {e}")
    
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
        
        # 從摘要中提取會議URL (如果有的話)
        url = ""
        lines = summary_text.strip().split('\n')
        for i, line in enumerate(lines):
            if '[會議影片連結]' in line and i > 0:
                url_match = line.strip()
                url = url_match.split('(')[1].split(')')[0] if '(' in url_match and ')' in url_match else ""
                # 移除這一行，避免在內容中重複顯示
                summary_text = '\n'.join(lines[:i] + lines[i+1:])
                break
        
        # 將 Markdown 格式轉換為 HTML
        try:
            import markdown
            
            # 處理標題問題：移除原始摘要中的標題，因為我們會在header中顯示
            lines = summary_text.strip().split('\n')
            if lines and lines[0].startswith('# '):
                # 移除第一行標題
                summary_text = '\n'.join(lines[1:]).strip()
                # 如果第二行也是標題（可能是翻譯），也移除它
                lines = summary_text.strip().split('\n')
                if lines and not lines[0].startswith('#') and not lines[0].startswith('*'):
                    summary_text = '\n'.join(lines[1:]).strip()
            
            # 轉換 Markdown 為 HTML
            html_content = markdown.markdown(summary_text)
            
            # 使用簡單直接的方式處理段落
            # 將 h2 標題作為段落分隔符
            html_parts = []
            current_part = ""
            in_section = False
            
            for line in html_content.split('\n'):
                if line.startswith('<h2>') and line.endswith('</h2>'):
                    # 如果已經在一個段落中，結束當前段落
                    if in_section:
                        html_parts.append(current_part + '</div>')
                    
                    # 開始一個新段落
                    section_title = line[4:-5]  # 去掉 <h2> 和 </h2>
                    section_class = "default"
                    
                    # 根據標題設置不同的類名
                    if "結論" in section_title or "Key Takeaways" in section_title:
                        section_class = "conclusion"
                    elif "會議主題" in section_title:
                        section_class = "meeting-topic"
                    elif "主要技術點" in section_title:
                        section_class = "tech-points"
                    elif "決策與共識" in section_title:
                        section_class = "decisions"
                    elif "時間規劃" in section_title or "里程碑" in section_title:
                        section_class = "timeline"
                    elif "未解決" in section_title or "技術挑戰" in section_title:
                        section_class = "challenges"
                    elif "後續行動" in section_title or "行動計劃" in section_title:
                        section_class = "action-plan"
                    
                    current_part = f'<div class="section-block {section_class}">'
                    current_part += f'<h2 class="section-title">{section_title}</h2>'
                    in_section = True
                else:
                    # 如果還沒有開始任何段落，創建一個默認段落
                    if not in_section:
                        current_part = '<div class="section-block default">'
                        in_section = True
                    
                    current_part += line
            
            # 添加最後一個段落
            if in_section:
                html_parts.append(current_part + '</div>')
            
            # 組合所有段落
            html_content = ''.join(html_parts)
            
            # 如果沒有任何段落，將整個內容放在一個默認段落中
            if not html_parts:
                html_content = f'<div class="section-block default">{html_content}</div>'
            
        except ImportError:
            # 如果 markdown 模組不可用，進行簡單的轉換
            html_content = summary_text.replace('\n', '<br>')
            html_content = html_content.replace('# ', '<h1>')
            html_content = html_content.replace('## ', '<h2>')
            html_content = html_content.replace('### ', '<h3>')
            html_content = f'<div class="section-block default">{html_content}</div>'
        
        # 創建 HTML 模板
        html_template = f"""
        <!DOCTYPE html>
        <html lang="zh-TW">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{meeting_title}</title>
            <style>
                body {{
                    font-family: 'Roboto', 'Microsoft JhengHei', sans-serif;
                    background-color: #f8f9fa;
                    color: #333;
                    margin: 0;
                    padding: 0;
                    line-height: 1.6;
                }}
                header {{
                    text-align: center;
                    padding: 30px 20px;
                    background: linear-gradient(135deg, #4b6cb7, #182848);
                    color: #fff;
                    position: relative;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                    border-radius: 10px 10px 0 0;
                }}
                .video-link {{
                    display: inline-block;
                    margin: 10px 0;
                    padding: 8px 15px;
                    background-color: rgba(255, 255, 255, 0.2);
                    color: #fff;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: 500;
                    transition: all 0.3s ease;
                    border: 1px solid rgba(255, 255, 255, 0.3);
                }}
                .video-link:hover {{
                    background-color: rgba(255, 255, 255, 0.3);
                    transform: translateY(-2px);
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
                .video-link i {{
                    margin-right: 5px;
                }}
                header h1 {{
                    font-size: 2.2rem;
                    margin: 0 0 10px 0;
                    letter-spacing: 0.5px;
                }}
                header p {{
                    font-size: 1.1rem;
                    margin: 0;
                    opacity: 0.9;
                }}
                header img {{
                    max-width: 35%;
                    height: auto;
                    margin-bottom: 15px;
                }}
                main {{
                    max-width: 900px;
                    margin: 30px auto;
                    padding: 0 20px;
                }}
                .content-container {{
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
                    padding: 30px;
                    margin-bottom: 30px;
                }}
                .section-block {{
                    background-color: #fff;
                    padding: 25px;
                    border-radius: 8px;
                    margin-bottom: 25px;
                    border-left: 5px solid #4b6cb7;
                    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
                    transition: transform 0.2s ease, box-shadow 0.2s ease;
                }}
                .section-block:hover {{
                    transform: translateY(-3px);
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
                }}
                /* 為不同段落設置不同的邊框顏色和背景 */
                .section-block.conclusion {{
                    border-left-color: #e74c3c;
                    background-color: #fff9f9;
                }}
                .section-block.meeting-topic {{
                    border-left-color: #3498db;
                    background-color: #f7fbff;
                }}
                .section-block.tech-points {{
                    border-left-color: #2ecc71;
                    background-color: #f7fff9;
                }}
                .section-block.decisions {{
                    border-left-color: #f39c12;
                    background-color: #fffaf5;
                }}
                .section-block.timeline {{
                    border-left-color: #9b59b6;
                    background-color: #faf5ff;
                }}
                .section-block.challenges {{
                    border-left-color: #e67e22;
                    background-color: #fff8f2;
                }}
                .section-block.action-plan {{
                    border-left-color: #1abc9c;
                    background-color: #f5fffc;
                }}
                .section-title {{
                    font-size: 1.5rem;
                    margin-top: 0;
                    margin-bottom: 20px;
                    padding-bottom: 10px;
                    border-bottom: 2px solid #4b6cb7;
                    display: inline-block;
                }}
                /* 為不同段落標題設置對應的顏色 */
                .section-block.conclusion .section-title {{
                    color: #e74c3c;
                    border-bottom-color: #e74c3c;
                }}
                .section-block.meeting-topic .section-title {{
                    color: #3498db;
                    border-bottom-color: #3498db;
                }}
                .section-block.tech-points .section-title {{
                    color: #2ecc71;
                    border-bottom-color: #2ecc71;
                }}
                .section-block.decisions .section-title {{
                    color: #f39c12;
                    border-bottom-color: #f39c12;
                }}
                .section-block.timeline .section-title {{
                    color: #9b59b6;
                    border-bottom-color: #9b59b6;
                }}
                .section-block.challenges .section-title {{
                    color: #e67e22;
                    border-bottom-color: #e67e22;
                }}
                .section-block.action-plan .section-title {{
                    color: #1abc9c;
                    border-bottom-color: #1abc9c;
                }}
                .content-container ul {{
                    padding-left: 20px;
                }}
                .content-container li {{
                    margin-bottom: 10px;
                    position: relative;
                    list-style-type: none;
                    padding-left: 25px;
                }}
                .content-container li::before {{
                    content: "•";
                    position: absolute;
                    left: 0;
                    color: #4b6cb7;
                    font-size: 1.2rem;
                    font-weight: bold;
                }}
                .section-block.conclusion li::before {{ color: #e74c3c; }}
                .section-block.meeting-topic li::before {{ color: #3498db; }}
                .section-block.tech-points li::before {{ color: #2ecc71; }}
                .section-block.decisions li::before {{ color: #f39c12; }}
                .section-block.timeline li::before {{ color: #9b59b6; }}
                .section-block.challenges li::before {{ color: #e67e22; }}
                .section-block.action-plan li::before {{ color: #1abc9c; }}
                
                .content-container p {{
                    margin-bottom: 15px;
                    line-height: 1.7;
                }}
                .content-container strong {{
                    color: #2c3e50;
                    font-weight: bold;
                }}
                footer {{
                    text-align: center;
                    padding: 25px 20px;
                    background-color: #f0f2f5;
                    color: #666;
                    border-radius: 0 0 10px 10px;
                    border-top: 1px solid #e0e0e0;
                }}
                footer img {{
                    max-width: 35%;
                    height: auto;
                    margin-bottom: 15px;
                }}
                footer p {{
                    margin: 5px 0;
                    font-size: 0.95rem;
                }}
                footer a {{
                    color: #4b6cb7;
                    text-decoration: none;
                    font-weight: bold;
                }}
                footer a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <header>
                <img src="https://i.imgur.com/0LXUWvj.png" alt="會議摘要圖示">
                <h1>{meeting_title}</h1>
                {f'<a href="{url}" class="video-link" target="_blank"><i>▶</i> 會議影片超連結</a>' if url else ''}
            </header>
            <main>
                <div class="content-container">
                    {html_content}
                </div>
            </main>
            <footer>
                <img src="https://i.imgur.com/0LXUWvj.png" alt="會議摘要圖示">
                <p>此摘要由 AI 輔助生成</p>
                <p>如有任何問題或需要更多詳細資訊，請聯繫 ITR 小組</p>
            </footer>
        </body>
        </html>
        """
        
        return html_template
    
    def save_email_html(self, summary, output_path, meeting_title=None):
        """
        將會議摘要保存為 Email HTML 文件
        
        Args:
            summary (dict): 包含摘要內容的字典
            output_path (str): 輸出文件路徑
            meeting_title (str, optional): 會議標題
        """
        if summary["status"] != "success":
            print(f"錯誤: 無法生成 Email HTML，摘要生成失敗")
            return
        
        # 獲取會議URL
        url = ""
        if meeting_title:
            url = meeting_list.get_url_by_meeting_name(meeting_title)
        
        html_content = self.generate_email_html(summary["summary"], meeting_title)
        
        # 如果有URL但HTML中沒有包含，手動添加
        if url and "會議影片超連結" not in html_content:
            html_content = html_content.replace(
                f'<h1>{meeting_title}</h1>',
                f'<h1>{meeting_title}</h1>\n<a href="{url}" class="video-link" target="_blank"><i>▶</i> 會議影片超連結</a>'
            )
        
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