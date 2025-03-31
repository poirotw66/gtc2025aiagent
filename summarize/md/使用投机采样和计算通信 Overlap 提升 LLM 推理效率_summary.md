# 使用投机采样和计算通信 Overlap 提升 LLM 推理效率
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E4%BD%BF%E7%94%A8%E6%8A%95%E6%9C%BA%E9%87%87%E6%A0%B7%E5%92%8C%E8%AE%A1%E7%AE%97%E9%80%9A%E4%BF%A1%20Overlap%20%E6%8F%90%E5%8D%87%20LLM%20%E6%8E%A8%E7%90%86%E6%95%88%E7%8E%87&tab.catalogallsessionstab=16566177511100015Kus#/session/1727598580103001ix9j)
# 使用投機採樣和計算通信 Overlap 提升 LLM 推理效率

## Key Takeaways
本次分享主要介紹了百川智能在 GDC2025 上關於提升 LLM 推理效率的兩項技術：投機採樣（Speculative Sampling）和計算通信 Overlap。投機採樣利用 Decode 階段的算力冗餘，通過 Draft Model 生成多個候選 Token 並行驗證，充分利用算力且不會增加太多延遲。計算通信 Overlap 則旨在提升低端卡上 GPU 的利用率，通過將請求切分並重疊計算和通信過程來優化性能。
### 重點摘要：
*   **投機採樣 (Speculative Sampling):** 利用 Draft Model 並行生成多個候選 Token，並通過大模型驗證，提高 Token 生成效率。
*   **Clover 模型結構:** 在美都莎 (Medusa) 結構基礎上進行改進，通過 TransformerLayer 收集全局信息，LegistRN 的 Attention 結構不斷吸收新 Token 信息，輔助下一 Token 的預測。
*   **動態 Token 樹構建:** 根據 Draft Model 預測的概率動態調整 Token 樹的寬度和深度，以最佳方式命中更多 Token。
*   **計算通信 Overlap:** 將請求切分成多段，並重疊計算和通信過程，提升 GPU 利用率，尤其在低端卡上效果顯著。
### Topic: LLM 推理優化，投機採樣，計算通信 Overlap

## 會議主題
會議主要探討了如何通過投機採樣和計算通信 Overlap 兩種技術來提升 LLM 的推理效率。投機採樣側重於模型結構的優化，通過 Draft Model 並行生成候選 Token，減少大模型的調用次數。計算通信 Overlap 則側重於工程實現的優化，通過重疊計算和通信過程，提升 GPU 的利用率。

## 主要技術點
*   **投機採樣原理:** 利用 Draft Model 並行生成 N+2, N+3, N+4 等多個 Token，然後同時扔給大模型進行驗證，一次性通過多個 Token，提高推理速度。
*   **Draft Model 的選擇:** 比較了獨立小模型、大模型額外子結構、外部數據增強等方案，最終選擇大模型的外子結構，並在此基礎上進行改進。
*   **Clover 模型結構:**
    *   TransformerLayer: 負責收集更全局的信息。
    *   LegistRN 的 Attention 結構: 負責不斷吸收新 Token 的信息到全局信息，輔助下一 Token 的預測。
*   **動態 Token 樹構建:** 根據 Draft Model 預測的概率動態調整 Token 樹的寬度和深度，以最佳方式命中更多 Token。
*   **Token Tree Mask 優化:** 將二維的 Token Tree Mask 通過算法簡化為一維，節省存儲空間。
*   **算子優化:** 基於 CUDA Core 和 Tensor Core 實現 Attention 算子，並採用窗口 Prefetch 等技術，提升性能。
*   **計算通信 Overlap:** 將請求切分成多段，並重疊計算和通信過程，提升 GPU 利用率。
*   **量化傳輸:** 通過量化傳輸方案，讓整個通信佔比盡量接近計算佔比，提高計算通信 Overlap 的收益。

## 決策與共識
*   採用投機採樣技術，利用 Draft Model 並行生成候選 Token，提高推理速度。
*   選擇大模型的外子結構作為 Draft Model，並在此基礎上進行改進，例如 Clover 模型結構。
*   採用動態 Token 樹構建策略，根據 Draft Model 預測的概率動態調整 Token 樹的寬度和深度。
*   採用計算通信 Overlap 技術，將請求切分成多段，並重疊計算和通信過程，提升 GPU 利用率。

## 時間規劃與里程碑
*   Clover 第一版本已上線，在各個任務數據上都超過了 Medusa，Token 命中率提升 50% 以上，端到端提升速度在 30%。
*   持續進行模型結構的升級，例如 Clover2。
*   持續進行工程結構的落地，例如 Token Tree Mask 優化、算子優化、計算通信 Overlap 等。

## 未解決的技術挑戰
*   在一些極端情況下，例如低端卡通信佔比非常高，或者 NVLink 卡計算佔比特別低，計算通信 Overlap 的效果可能不佳。
*   Otention 計算量的不平衡，SequenceR 第二段的計算往往比第一段階段需要更高，需要通過一些策略調整整個第二段的計算的 Token 佔比。
*   Otention 和 MLP 通訊之間的不平衡，需要設計更複雜的簽生方式。

## 後續行動計劃
*   繼續優化 Clover 模型結構，例如 Clover2。
*   繼續優化工程結構，例如 Token Tree Mask 優化、算子優化、計算通信 Overlap 等。
*   針對不同的硬件平台和模型，調整投機採樣和計算通信 Overlap 的策略，以達到最佳性能。
*   探索更多提升 LLM 推理效率的技術，例如模型壓縮、量化、剪枝等。
