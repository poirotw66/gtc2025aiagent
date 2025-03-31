# NVIDIA 全面赋能端到端自动驾驶
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=NVIDIA%20%E5%85%A8%E9%9D%A2%E8%B5%8B%E8%83%BD%E7%AB%AF%E5%88%B0%E7%AB%AF%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6&search=NVIDIA+%E5%85%A8%E9%9D%A2%E8%B5%8B%E8%83%BD%E7%AB%AF%E5%88%B0%E7%AB%AF%E8%87%AA%E5%8A%A8%E9%A9%BE%E9%A9%B6&tab.catalogallsessionstab=16566177511100015Kus#/session/1736179124568001qocF)
# NVIDIA 全面賦能端到端自動駕駛

## Key Takeaways
本次會議主要介紹 NVIDIA 如何在端到端自動駕駛領域提供全面賦能，涵蓋 World Model 的應用、神經重建引擎 (NRE) 以及訓練優化等方面。
### 重點摘要：
*   **World Model:** 介紹了 World Model 的起源、在自動駕駛中的應用，以及 NVIDIA Cosmos 平台如何利用 World Model 進行後訓練和重建。
*   **神經重建引擎 (NRE):** 闡述了 NRE 的用途、功能，以及如何利用 NRE 進行三維重建和渲染，並結合生成式 AI 提升新視角渲染效果。
*   **訓練優化:** 分享了 NVIDIA DevTech Team 在圖片訓練、影片訓練以及 Loss 計算方面的優化策略。
### Topic: 自動駕駛、World Model、神經重建、訓練優化

## 會議主題
會議主要圍繞 NVIDIA 在自動駕駛領域的技術創新和解決方案展開，重點包括 World Model 的應用、神經重建引擎 (NRE) 的能力，以及針對自動駕駛模型訓練的優化策略。

## 主要技術點
*   **World Model:**
    *   World Model 的起源和概念，以及與人腦認知科學中 Mental Model 的類比。
    *   World Model 在自動駕駛中的應用，包括輸入 (感測器數據、控制指令等) 和輸出 (生成影片、規劃、動作預測等)。
    *   保證生成影片真實性的方法，包括跨相機一致性和時序一致性。
    *   NVIDIA Cosmos 平台如何利用 World Model 進行後訓練，生成 Counter Case，以及修復重建影片。
*   **神經重建引擎 (NRE):**
    *   NRE 的用途，包括三維重建和渲染，以及在閉環仿真中的應用。
    *   NRE 對各類感測器的準確建模，包括相機和雷達。
    *   NRE 對多感測器同時重建的支援。
    *   NRE 結合生成式 AI 提升新視角渲染效果，解決重建瑕疵問題。
*   **訓練優化:**
    *   圖片訓練 Pipeline 的優化，包括 GPU 加速、達利 (DALI) 優化、自定義算子等。
    *   影片訓練 Pipeline 的設計，包括 On-Demand Video Decoding、最小解碼代價、顯存優化等。
    *   Loss 計算 Batching 的方法，利用 RegBatch 處理 Non-Uniform 的 Ground Truth，並與各種 Loss 函數相容。

## 決策與共識
*   利用 World Model 進行自動駕駛的後訓練和重建，提升模型的泛化能力和魯棒性。
*   採用 NRE 進行高真實度的三維重建和渲染，為閉環仿真提供更可靠的數據。
*   通過圖片訓練、影片訓練和 Loss 計算等方面的優化，提升模型訓練的效率和效能。
*   利用 MIG 和 GPU Scheduling 技術，實現高效的端到端模型部署和資源分配。

## 時間規劃與里程碑
*   持續優化 World Model，提升生成影片的真實性和一致性。
*   不斷完善 NRE 的功能，提升重建和渲染的品質和效率。
*   持續探索新的訓練優化方法，提升模型訓練的速度和效能。
*   不斷迭代 Shall 平台，提供更強大的算力和更完善的軟體支援。

## 未解決的技術挑戰
*   如何進一步提升 World Model 生成影片的真實性和一致性，特別是在複雜場景下。
*   如何進一步提升 NRE 的重建和渲染效率，並降低對計算資源的需求。
*   如何更好地處理 Non-Uniform 的 Ground Truth，提升 Loss 計算 Batching 的效能。
*   如何在端到端模型中更好地控制精度，實現更高的部署效果。

## 後續行動計劃
*   繼續研究和開發 World Model，探索其在自動駕駛領域的更多應用。
*   持續優化 NRE，提升其在閉環仿真中的價值。
*   將訓練優化方法應用於更多模型，提升整體訓練效能。
*   不斷完善 Shall 平台，為自動駕駛的發展提供更強大的支援。
