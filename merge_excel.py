import pandas as pd

# 讀取 A 和 B 檔案
file_a = "研討會會議清單.xlsx"  # A 檔案名稱
file_b = "GTC_ALL (2) (1).xlsx"  # B 檔案名稱

df_a = pd.read_excel(file_a)  # 讀取 A 檔案
df_b = pd.read_excel(file_b)  # 讀取 B 檔案

# 確保欄位名稱一致，避免因大小寫或空格不同而匹配失敗
column_meeting = "Meeting"  # 會議名稱欄位
column_tech_level = "Topic"  # 技術等級欄位

# 透過「會議名稱」進行左合併 (left join)，將「技術等級」對應到 A 檔案
df_merged = df_a.merge(df_b[[column_meeting, column_tech_level]], on=column_meeting, how="left")

# 儲存合併後的 A 檔案
output_file = "研討會會議清單_更新後.xlsx"
df_merged.to_excel(output_file, index=False)

print(f"處理完成！結果已儲存至 {output_file}")
