"""
研討會會議清單讀取工具 - 將 Excel 檔案轉換為會議名稱到URL的映射
"""

import os
import pandas as pd
from pathlib import Path

class MeetingListReader:
    """讀取研討會會議清單並提供會議名稱到URL的映射"""
    
    def __init__(self, excel_path=None):
        """
        初始化會議清單讀取器
        
        Args:
            excel_path (str, optional): Excel 檔案路徑，如果為 None 則使用預設路徑
        """
        if excel_path is None:
            # 預設路徑為專案根目錄下的研討會會議清單.xlsx
            project_root = Path(__file__).parent.parent
            excel_path = os.path.join(project_root, "研討會會議清單.xlsx")
        
        self.excel_path = excel_path
        self.meeting_urls = {}  # 簡化為會議名稱到URL的映射
        self.loaded = False
    
    def load_meeting_list(self):
        """
        讀取會議清單 Excel 檔案並建立會議名稱到URL的映射
        
        Returns:
            dict: 會議名稱到URL的映射
        """
        try:
            # 讀取 Excel 檔案
            df = pd.read_excel(self.excel_path)
            
            # 確保必要的欄位存在
            required_columns = ["Meeting", "URL"]
            missing_columns = [col for col in required_columns if col not in df.columns]
            
            if missing_columns:
                print(f"警告: Excel 檔案缺少以下必要欄位: {', '.join(missing_columns)}")
                return {}
            
            # 建立會議名稱到URL的映射
            self.meeting_urls = {}
            for _, row in df.iterrows():
                meeting_name = str(row["Meeting"])
                url = str(row["URL"]) if not pd.isna(row["URL"]) else ""
                self.meeting_urls[meeting_name] = url
            
            self.loaded = True
            print(f"成功讀取 {len(self.meeting_urls)} 筆會議URL資料")
            return self.meeting_urls
            
        except Exception as e:
            print(f"讀取會議清單時發生錯誤: {e}")
            return {}
    
    def get_meeting_urls(self):
        """
        獲取會議名稱到URL的映射
        
        Returns:
            dict: 會議名稱到URL的映射
        """
        if not self.loaded:
            return self.load_meeting_list()
        return self.meeting_urls
    
    def get_url_by_meeting_name(self, meeting_name):
        """
        根據會議名稱獲取URL
        
        Args:
            meeting_name (str): 會議名稱
            
        Returns:
            str: 會議URL，如果找不到則返回空字串
        """
        if not self.loaded:
            self.load_meeting_list()
        
        return self.meeting_urls.get(meeting_name, "")


# 單例模式，方便其他模組直接導入使用
meeting_list = MeetingListReader()

# 使用範例
if __name__ == "__main__":
    # 讀取會議清單
    meeting_urls = meeting_list.get_meeting_urls()
    
    # 顯示所有會議及其URL
    for meeting_name, url in meeting_urls.items():
        print(f"會議名稱: {meeting_name}")
        print(f"URL: {url}")
        print("-" * 50)