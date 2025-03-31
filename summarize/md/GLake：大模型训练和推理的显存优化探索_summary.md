# GLake：大模型训练和推理的显存优化探索
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=GLake%EF%BC%9A%E5%A4%A7%E6%A8%A1%E5%9E%8B%E8%AE%AD%E7%BB%83%E5%92%8C%E6%8E%A8%E7%90%86%E7%9A%84%E6%98%BE%E5%AD%98%E4%BC%98%E5%8C%96%E6%8E%A2%E7%B4%A2&tab.catalogallsessionstab=16566177511100015Kus#/session/1727157704835001TEfI)
# GLake：大模型訓練和推理的顯存優化探索

## Key Takeaways
本次會議主要介紹了螞蟻 AI Infra 推理引擎團隊在過去兩年時間裡，針對大模型訓練和推理所做的一些顯存優化工作，包括訓練階段的 GM-Lake 和推理階段的 VTensor 及 LayerKV。
### 重點摘要：
*   **GM-Lake:** 解決大規模訓練過程中的顯存碎片問題，已發表在 S Plus 24 上。
*   **VTensor:** 提供 Pageless 的 Tensor 管理框架，提供更大的靈活性。
*   **LayerKV:** 通過 LayerWise 的 KVCatch 管理來優化首次延遲，並在滿足特定 SLO 情況下提升整體吞吐。
### Topic: 顯存優化、大模型訓練、大模型推理

## 會議主題
會議主要探討了如何通過優化顯存管理，提升大模型訓練和推理的效率，包括解決顯存碎片問題、提供更靈活的 Tensor 管理框架以及優化首次延遲等。

## 主要技術點
*   **GM-Lake:**
    *   **Background and Motivation:** 模型規模增長速度遠超 GPU 顯存增長速度，導致嚴重的內存牆。Recomputing 技術雖然可以提升顯存使用效率，但會導致顯存分配不規律，產生大量碎片。
    *   **Stitch API:** 利用 CUDA VMM API，將虛擬顯存和物理顯存的管理拆分開，先創建物理顯存，再根據需要分配虛擬顯存，並映射物理顯存到虛擬顯存上。
    *   **多級顯存池:** 根據請求大小在多級顯存池中尋找最匹配的 Block，並通過 Stitch 操作拼接 Block，高效服用物理顯存。
*   **VTensor:**
    *   **Pageless Tensor 管理框架:** 解決 PageTableTension 將顯存管理和 Attention Kernel 實現緊密耦合的問題，以及提前映射大量顯存導致資源浪費的問題。
    *   **VTensorManager:** 高效顯存管理，解決碎片的核心組件，包含 VTensorScheduler、VTensorPort 和 VTensorOperation。
    *   **Layer 維度 KVCatch 管理:** 將 Layer 維度加入到 KVCatch 管理中，減少每個請求每層最後一個兩兆幣的浪費。
*   **LayerKV:**
    *   **LayerWise KVCatch 管理:** 支持分層申請 KVCatch 的顯存，減少整體顯存的依賴，並在 Prefill 階段支持分層將產生的 KVCatch 臨時傳輸到 CPU 上。
    *   **Scheduler 調度策略:** 基於顯存壓力和對列的請求長度動態決定是否激活 LayerKV。

## 決策與共識
*   通過 GM-Lake 解決訓練過程中的顯存碎片問題，提升顯存利用率。
*   通過 VTensor 提供更靈活的 Tensor 管理框架，解耦顯存管理和 Attention Kernel 實現。
*   通過 LayerKV 優化首次延遲，並在滿足特定 SLO 情況下提升整體吞吐。

## 時間規劃與里程碑
*   GM-Lake 已發表在 S Plus 24 上。
*   VTensor 和 LayerKV 已在螞蟻 AI Infra 推理引擎團隊內部使用。

## 未解決的技術挑戰
*   VMM 接口中提供的最小的物理塊的力度是兩兆幣，如果按照 VMM 中每層 layer 使用不同的 Tensor 來存放每層不同的 KVCatch，會導致每個請求每層最後的一個兩兆幣的物理塊可能有比較大的浪費。

## 後續行動計劃
*   繼續優化 GM-Lake，提升顯存利用率和訓練效率。
*   繼續優化 VTensor 和 LayerKV，提升推理效率和吞吐。
*   將 GM-Lake、VTensor 和 LayerKV 應用於更多的大模型訓練和推理場景。
