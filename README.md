# 會議逐字稿總結工具

這是一個基於Google Gemini 2.0 API的自動化會議逐字稿總結工具。該工具旨在幫助用戶快速從會議記錄中提取關鍵資訊，生成結構化的報告，並支援多種輸出格式，方便後續的分享與存檔。

## 功能特點

- **智能分析**：使用Google Gemini 2.0 AI模型，深入分析會議內容。
- **關鍵資訊提取**：自動提取會議中的主要議題、決策、任務分配和後續行動計劃。
- **多語言支援**：支援多語言逐字稿的處理與總結。
- **靈活輸出**：生成多種格式的報告，包括JSON、TXT和Markdown，滿足不同需求。
- **模組化設計**：允許用戶根據需求單獨執行特定處理步驟。
- **高效處理**：支援批量處理多個逐字稿，提升工作效率。

## 安裝要求

- **Python 版本**：Python 3.8 或更高版本
- **依賴套件**：
    - Google Generative AI Python SDK
    - 其他依賴詳見 `requirements.txt`

## 安裝步驟

1. **克隆儲存庫**：
     ```bash
     git clone https://github.com/your-repo/gtc2025aiagent.git
     cd gtc2025aiagent
     ```

2. **安裝依賴**：
     使用以下命令安裝所需的Python套件：
     ```bash
     pip install -r requirements.txt
     ```

3. **配置API金鑰**：
     確保已取得Google Gemini 2.0 API金鑰，並將其配置為環境變數：
     ```bash
     export GOOGLE_API_KEY="your_api_key_here"
     ```

4. **準備輸入資料**：
     - 將會議逐字稿放置於 `./data/transcript/` 資料夾。
     - 將主題演講逐字稿放置於 `./data/keynote/` 資料夾。
     - 確保會議清單Excel檔案位於根目錄，並命名為 `研討會會議清單.xlsx`。

5. **執行工具**：
     按照[使用說明](#usage)中的指引執行工具。

## 支援的輸入格式

- **逐字稿**：純文字檔案（.txt）
- **會議清單**：Excel檔案（.xlsx）

## 注意事項

- 確保輸入資料的格式正確，避免因格式錯誤導致處理失敗。
- 若需處理大量逐字稿，建議檢查系統資源是否充足。

## 常見問題

1. **如何處理API金鑰無效的問題？**
     - 確認API金鑰是否正確，並檢查是否已啟用相關API服務。

2. **工具執行速度較慢？**
     - 確保網路連線穩定，並檢查是否有足夠的系統資源。

3. **輸出報告格式不符合預期？**
     - 檢查輸入資料是否完整，並參考範例檔案進行格式校正。

如有其他問題，請參考[官方文件](https://developers.google.com/gemini)或提交Issue至本儲存庫。

```bash
pip install -r requirements.txt
```
## Usage
### 一鍵執行所有處理步驟
使用排程腳本一次性執行所有處理步驟：
```bash
python run_all.py
# 您也可以自定義參數：
python run_all.py --transcript-dir "./data/transcript/" --keynote-dir "./data/keynote/" --excel-file "./研討會會議清單.xlsx" --output-dir "./report/" --topic-dir "./report/topic/"
```
### 個別執行處理步驟
您也可以個別執行處理步驟：
```bash
# 處理會議逐字稿
python batch_summarize_process.py -i "./data/transcript/" -o "./report/topic/"
# 處理主題演講逐字稿
python batch_summarize_process.py -i "./data/keynote/" -o "./report/topic/"
# 生成會議報告
python src/generate_meeting_report.py -i "./研討會會議清單.xlsx" -o "./report/topic/"
# 生成首頁
python src/generate_homepage.py -i "./研討會會議清單.xlsx" -o "./report/"

```