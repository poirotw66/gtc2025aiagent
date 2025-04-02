# 使用投機採樣和計算通信 Overlap 提升 LLM 推理效率
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E4%BD%BF%E7%94%A8%E6%8A%95%E6%9C%BA%E9%87%87%E6%A0%B7%E5%92%8C%E8%AE%A1%E7%AE%97%E9%80%9A%E4%BF%A1%20Overlap%20%E6%8F%90%E5%8D%87%20LLM%20%E6%8E%A8%E7%90%86%E6%95%88%E7%8E%87&tab.catalogallsessionstab=16566177511100015Kus#/session/1727598580103001ix9j)

## Key Takeaways
本次分享主要介紹了百川智能在 GDC2025 上關於提升 LLM 推理效率的技術，核心在於使用投機採樣和計算通信 Overlap。投機採樣利用 Decode 階段的算力冗餘，通過 Draft Model 生成多個候選 Token 並行驗證，充分利用算力且不增加太多延遲。計算通信 Overlap 則旨在提升低端卡上 GPU 的利用率，通過將請求切分並重疊計算和通信過程來優化性能。
### 重點摘要：
*   投機採樣原理：利用 Draft Model 並行生成多個候選 Token，並通過大模型驗證，一次性通過多個 Token。
*   Draft Model 的設計：從獨立小模型、大模型額外子結構、外部數據增強等多種方案中，選擇大模型的外子結構，並在此基礎上進行改進。
*   Clover 結構：通過 TransformerLayer 收集全局信息，LegistRN 的 Attention 結構不斷吸收新 Token 信息輔助下一 Token 的預測。
*   動態構建 Token 數：採用貪心策略，根據 Draft Model 預測的概率動態調整 Token Tree 的寬度和深度，最佳化 Token 命中率。
*   計算通信 Overlap：將請求切分成兩半，前一半進行 Otun 計算，後一半同時進行 Otun 計算，實現序列內維度的 Overlap。
### Topic:
*   LLM 推理優化
*   投機採樣
*   計算通信 Overlap

## 會議主題
會議主要探討了如何通過投機採樣和計算通信 Overlap 這兩種技術，提升 LLM 在推理階段的效率。投機採樣著重於利用算力冗餘，並行驗證多個 Token，而計算通信 Overlap 則旨在解決低端卡上通信瓶頸的問題。

## 主要技術點
*   **投機採樣 (Speculative Sampling):**
    *   利用 Decode 階段的算力冗餘，通過 Draft Model 生成多個候選 Token。
    *   大模型並行驗證候選 Token，充分利用算力且不增加太多延遲。
    *   傳統 AutoRegressive 結構是輸入一個 Token，大模型輸出一個 Token，投機採樣則是輸入一個 Token，並行驗證多個 Token。
*   **Draft Model 設計:**
    *   多種方案：獨立小模型、大模型額外子結構、外部數據增強。
    *   雲端優先考慮大模型的外子結構，一體機考慮獨立強模型。
    *   Clover 結構：TransformerLayer 收集全局信息，LegistRN 的 Attention 結構吸收新 Token 信息輔助預測。
*   **動態構建 Token 數:**
    *   貪心策略：大模型輸出 Token 後，Draft Model 生成 Next 加 2 的 Token。
    *   按照 Top 0.8 的概率進行篩選，保證 Token Tree 的深度往下發散。
    *   聯合概率：考慮當前概率和子節點概率，選取 Top N 個 Token。
    *   Token Tree 結構可變寬可變深，根據 Draft Model 預測概率動態變化。
*   **Clover 結構升級:**
    *   Loss 優化：引入 regressive loss，抑制 Clover 固定核問題，關注與主模型的一致性。
    *   Token 信息前置：將第一個 Head 的信息提前加入到 Transformer Layer 之前。
    *   RN 結構改進：不僅考慮 Hidden State 信息，同時考慮 Input 信息。
    *   增加 Transformer Layer 層數：提高信息提取能力。
*   **工程結構落地:**
    *   Preview 階段和 Decode 階段。
    *   Draft Model 實現模型預測、輸出構建、多 Batch 下高效 Sample、構建 Tree Mask。
    *   Decode 階段支持並行驗證、Tree Mask、KV Cache 管理、MLP 並行跑。
    *   Sample 階段進行新型優化。
*   **Tree Mask 優化:**
    *   將二維矩陣的 Tree Mask 通過算法簡化為一維。
    *   通過比較大小判斷 Tree Mask 的結構，節省存儲量。
*   **算子優化:**
    *   實現基於 CUDA Core 和 Tensor Core 的兩個版本。
    *   Tensor Core 版本節省了窗口 Prefetch，在 GQV 場景下收益明顯。
*   **Sample 優化:**
    *   並行化 Sample，將 Sample 參數按照 Tree 結構直接複製 N File。
    *   支持動態調整 Token 數。
*   **計算通信 Overlap:**
    *   將請求切分成兩半，前 16k 先進行 Otun 計算，後 16k 同時進行 Otun 計算。
    *   保證每一層的前 16k 先計算，後 16k 後計算，保證序列計算一致性。
    *   針對計算密集型和通信密集型場景進行優化。
    *   量化傳輸方案，降低通信占比。
    *   拆分 QKV 計算或 GITUP 計算，減少 Kernel Launch 的影響。
    *   調整 Token 占比，結合 Token Prefill 技術，平衡計算開銷。
    *   Otention 和 MLP 合併計算，設計更複雜的簽生方式。

## 決策與共識
*   採用投機採樣和計算通信 Overlap 提升 LLM 推理效率。
*   選擇大模型的外子結構作為 Draft Model 的設計方案。
*   採用 Clover 結構，並不斷進行模型結構升級。
*   通過工程結構落地，實現高效的並行驗證和 Sample。
*   針對不同場景進行計算通信 Overlap 優化。

## 時間規劃與里程碑
*   Clover 第一版本上線，在各個任務數據上超過每都沙，Token 命中率提升 50% 以上，端到端提升速度在 30%。
*   持續進行模型結構升級，推出 Clover2，在各個數據上超越 EGO，最大命中提升 7.7%，端到端最大提升速度 9.3%。
*   工程結構落地，實現高效的並行驗證和 Sample。

## 未解決的技術挑戰
*   低端卡上的通信瓶頸仍然存在，需要進一步優化計算通信 Overlap。
*   Token 數的動態調整策略需要進一步完善，以適應不同的應用場景。
*   模型結構升級需要持續進行，以逼近 EGO 的效果，並保持輕量化的優勢。

## 後續行動計劃
*   繼續優化 Clover 結構，提升 Token 命中率和推理速度。
*   完善計算通信 Overlap 方案，解決低端卡上的通信瓶頸。
*   探索更多模型結構升級方案，逼近 EGO 的效果，並保持輕量化的優勢。
*   將相關技術應用於更多 LLM 模型，提升推理效率。
