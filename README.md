# 會議逐字稿總結工具

這是一個使用Google Gemini 2.0 API自動總結會議逐字稿的工具。該工具可以從會議記錄中提取關鍵資訊，包括主要議題、決策、任務分配和後續行動。

## 功能特點

- 使用Google Gemini 2.0 AI模型分析會議內容
- 提取會議中的關鍵議題和決策
- 識別任務分配和責任人
- 總結未解決問題和後續行動計劃
- 支援多種輸出格式(JSON, TXT, Markdown)

## 安裝要求

- Python 3.8+
- Google Generative AI Python SDK

## 安裝步驟

1. 克隆此儲存庫
2. 安裝依賴:

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