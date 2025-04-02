# NVIDIA 全面賦能端到端自動駕駛
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=NVIDIA%20%E5%85%A8%E9%9D%A2%E8%B5%8B%E8%83%BD%E7%AB%AF%E5%88%B0%E7%AB%AF%E8%87%AA%E5%8A%A8%E9%A9%97%E9%A9%B6&search=NVIDIA+%E5%85%A8%E9%9D%A2%E8%B5%8B%E8%83%BD%E7%AB%AF%E5%88%B0%E7%AB%AF%E8%87%AA%E5%8A%A8%E9%A9%97%E9%A9%B6&tab.catalogallsessionstab=16566177511100015Kus#/session/1736179124568001qocF)
NVIDIA 全面賦能端到端自動駕駛

## Key Takeaways
本次會議主要介紹 NVIDIA 在端到端自動駕駛領域的全面賦能，涵蓋 World Model、神經重建引擎 (NRE) 以及訓練優化等方面。
### 重點摘要：
*   **World Model:** 介紹 World Model 的起源、在自動駕駛上的應用，以及 NVIDIA Cosmos 如何在自動駕駛場景中賦能。
*   **神經重建引擎 (NRE):** 介紹 NVIDIA 的神經重建引擎，包括其用途和當前版本具備的能力，以及如何支援閉環仿真。
*   **訓練優化:** 介紹 NVIDIA DevTech Team 在自駕領域所做的一些訓練優化，包括圖片訓練 Pipeline、影片訓練 Pipeline 以及如何將 Loss 計算 Batch 起來。
### Topic:
*   World Model
*   神經重建引擎 (NRE)
*   訓練優化
*   端到端自動駕駛

## 會議主題
會議主要探討了 NVIDIA 如何透過 World Model、神經重建引擎 (NRE) 以及訓練優化等技術，全面賦能端到端自動駕駛，並提升自動駕駛系統的性能和安全性。

## 主要技術點
*   **World Model:**
    *   World Model 的起源和發展，以及其在自動駕駛中的應用。
    *   World Model 如何利用感測器輸入、控制模組和條件資訊生成更貼近現實情況的影片。
    *   如何保證生成影片的真實性，包括跨相機的一致性和時序上的一致性。
    *   NVIDIA Cosmos 如何在自動駕駛場景中生成 Counter Case，並作為重建過程中的 Fixer。
*   **神經重建引擎 (NRE):**
    *   NRE 的用途和基於神經輻射場 (NERF) 和 3D Gaussian 的三維場景表示。
    *   NRE 如何從真實採集的相機二維圖像和雷射點雲中重新渲染出具有真實感的二維圖像和點雲。
    *   NRE 如何支援閉環仿真，並對各類感測器進行準確建模。
    *   NRE 如何利用生成式 AI 提供更好的新視角渲染結果，並修復有瑕疵的渲染圖像。
*   **訓練優化:**
    *   如何利用 DALI 設計 Auto Model Training 的最佳實踐，並加速圖片訓練。
    *   如何實現 On Demand Video Decoding，並減少影片訓練的儲存和頻寬需求。
    *   如何將 Loss 計算 Batch 起來，並放在 GPU 上加速計算。

## 決策與共識
*   NVIDIA 致力於透過 World Model、神經重建引擎 (NRE) 以及訓練優化等技術，全面賦能端到端自動駕駛。
*   NVIDIA Cosmos 可以生成 Counter Case，並作為重建過程中的 Fixer，為自動駕駛系統提供更全面的測試和驗證。
*   NRE 可以支援閉環仿真，並對各類感測器進行準確建模，為自動駕駛系統提供更真實的仿真環境。
*   透過 DALI 和 On Demand Video Decoding 等技術，可以加速圖片和影片訓練，並減少儲存和頻寬需求。
*   將 Loss 計算 Batch 起來，並放在 GPU 上加速計算，可以提升模型訓練的效率。

## 時間規劃與里程碑
*   持續開發和優化 World Model、神經重建引擎 (NRE) 以及訓練優化等技術。
*   將 NVIDIA Cosmos 應用於更多自動駕駛場景，並提供更全面的測試和驗證。
*   將 NRE 應用於更多仿真環境，並提供更真實的仿真結果。
*   持續優化 DALI 和 On Demand Video Decoding 等技術，並提升圖片和影片訓練的效率。
*   將 Loss 計算 Batch 起來的技術應用於更多模型，並提升模型訓練的效率。

## 未解決的技術挑戰
*   如何進一步提升生成影片的真實性，包括跨相機的一致性和時序上的一致性。
*   如何進一步提升 NRE 的渲染品質，並減少渲染瑕疵。
*   如何進一步優化訓練 Pipeline，並提升模型訓練的效率。
*   如何更好地控制端到端模型的精度，並實現理想的部署效果。

## 後續行動計劃
*   持續研究和開發 World Model、神經重建引擎 (NRE) 以及訓練優化等技術。
*   與更多合作夥伴合作，共同推動端到端自動駕駛的發展。
*   將 NVIDIA 的技術應用於更多自動駕駛場景，並為自動駕駛行業提供更全面的解決方案。
