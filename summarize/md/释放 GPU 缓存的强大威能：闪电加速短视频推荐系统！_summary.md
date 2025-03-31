# 释放 GPU 缓存的强大威能：闪电加速短视频推荐系统！
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E9%87%8A%E6%94%BE%20GPU%20%E7%BC%93%E5%AD%98%E7%9A%84%E5%BC%BA%E5%A4%A7%E5%A8%81%E8%83%BD%EF%BC%9A%E9%97%AA%E7%94%B5%E5%8A%A0%E9%80%9F%E7%9F%AD%E8%A7%86%E9%A2%91%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F%EF%BC%81&tab.catalogallsessionstab=16566177511100015Kus#/session/1727696079090001o2rO)
# 釋放 GPU 緩存的強大威能：閃電加速短視頻推薦系統！

## Key Takeaways
本次會議主要討論了如何通過 GPU Embedding Cache 技術來加速短視頻推薦系統，解決 CPU 算力瓶頸問題，充分利用 GPU 的算力。
### 重點摘要：
*   短視頻推薦系統面臨海量數據和用戶增長帶來的計算效率和實時性挑戰。
*   GPU 加速技術在推薦系統的召回和排序階段已得到廣泛應用。
*   新一代 GPU 架構（如 Ada）的引入，提升了計算密度，但也帶來了 CPU 算力滯後的問題。
*   通過將 Embedding 查詢階段從 CPU 卸載到 GPU，可以有效解決 CPU 瓶頸問題。
*   利用 GPU Embedding Cache，將高頻訪問的熱 Embedding 保留在 GPU 內存中，將低頻訪問的冷 Embedding 存儲在 CPU 內存或參數服務器中，提升 Embedding 查詢整體性能。
### Topic: GPU Embedding Cache、短視頻推薦系統、性能優化

## 會議主題
會議主要探討了如何利用 GPU Embedding Cache 技術，將 Embedding 查詢階段從 CPU 轉移到 GPU，以解決短視頻推薦系統中 CPU 算力瓶頸問題，提升系統性能。

## 主要技術點
*   **GPU Embedding Cache 設計：**
    *   將 Feature 經過編碼後形成數字 Slot 和 Sign。
    *   Embedding 是 Sign 的向量化表示。
    *   將相同 Dimension、DataType 和 Embedding Server 的數據放在一起形成 Group，去除業務相關性。
    *   將數據按照 Group 進行排序，方便 GPU 處理。
*   **GPU Embedding Cache 查詢流程：**
    *   收集 Sign 並進行 Batch 處理，減少 GPU Launch 次數。
    *   對 Batch 後的 Sign 進行去重，減少查詢量。
    *   查詢 GPU Cache，如果 Miss，則從遠端獲取 Embedding。
    *   將 Miss 的 Sign 交給 CPU 處理，CPU 從 Embedding Server 獲取 Embedding 並更新到 CPU Cache。
    *   CPU 將 Embedding 返回給 GPU，GPU 恢復 Paint Memory。
*   **分層存儲策略：**
    *   將高頻訪問的熱 Embedding 保留在 GPU 內存中。
    *   將低頻訪問的冷 Embedding 存儲在 CPU 內存或參數服務器中。
*   **優化策略：**
    *   使用 CUDA Graph 減少 Launch 次數。
    *   增加數據過期處理方案（FIFO、定期超時）。
    *   進行 Table Fusion，將小維度的 Table 擴充到大維度，減少 Cache 管理的複雜性。
    *   對 Embedding Cache 的更新進行線程控制，避免頻繁更新。

## 決策與共識
*   將 Embedding 查詢階段從 CPU 卸載到 GPU。
*   採用分層存儲策略，將熱 Embedding 放在 GPU Cache 中，冷 Embedding 放在 CPU 內存或參數服務器中。
*   通過 Batch 處理、去重等方式減少 GPU Launch 次數和查詢量。
*   使用 CUDA Graph、數據過期處理、Table Fusion 等優化策略提升性能。

## 時間規劃與里程碑
會議中未明確提及具體的時間規劃與里程碑。

## 未解決的技術挑戰
*   無法預先知道 Sign 的數量，導致 GPU 內存分配困難，需要提前運行程序獲取數據分佈情況，再設置 Cache 大小。
*   在 Query 和 Update 時存在鎖操作，需要考慮如何去除鎖或使用其他方式替換。

## 後續行動計劃
*   繼續優化 GPU Embedding Cache 的性能，降低 CPU 佔用率。
*   考慮動態分配 GPU 內存，解決 Cache 大小設置問題。
*   研究去除鎖操作的方案，提升 GPU 並行處理能力。
