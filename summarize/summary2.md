# 大規模言語モデル学習スケールのためのテレコムのケース

**1. 研討會主題與目標:**

本次研討會探討了 NTT Communications 如何利用其 GPU APN (GPU Accelerated Private Network) 的概念，結合 NVIDIA 的 Nemo 和 Megatron 等分散式學習框架，在分散式資料中心環境下進行大規模語言模型 (LLM) 的訓練。目標是解決因生成式 AI 應用激增而導致的 GPU 資源短缺問題，並展示透過 APN 連接分散式 GPU 資源的有效性。

**2. 主要技術討論點:**

*   **GPU APN 概念:** 利用 NTT Communications 的 ION APN 網路連接分散在不同資料中心的 GPU 資源，形成一個邏輯上的 GPU 叢集。
*   **分散式學習框架選型:** 評估了 NVIDIA 的 Nemo 和 Megatron 等分散式學習框架。Nemo 適合快速部署，而 Megatron 則提供更高的客製化程度。
*   **NVIDIA Nemo 和 Megatron:** 介紹了 Nemo 和 Megatron 的架構、優勢（支援多種模型架構、混合精度訓練、多種並行策略）以及使用上的注意事項（Nemo 正從 1.0 版本轉移到 2.0 版本，設定方式從 YAML 變為 Python 程式碼）。
*   **分散式學習策略:** 討論了資料並行、模型並行、pipeline 並行和 Tensor並行等分散式學習策略，以及如何在 Nemo 中設定這些策略。
*   **長距離通訊優化:** 使用 NVIDIA 的 NCCL (NVIDIA Collective Communications Library) 對長距離 RDMA 通訊進行優化。透過調整 NCCL 緩衝區大小和 QP (Queue Pair) 大小等參數，降低網路延遲對性能的影響。
*   **Custom LLM整合:** 說明如何將自有的 LLM 架構整合到 Nemo 框架中，包括資料預處理、模型定義、權重轉換等步驟。
*   **資料集準備:** 強調了在 Nemo 中使用 JSONL 格式，以及使用 `preprocess_data_for_megatron.py` 腳本進行資料前處理的重要性。

**3. 決策與共識:**

*   選擇 NVIDIA 的 Nemo 和 Megatron 作為分散式學習框架，並根據專案需求選擇合適的框架版本。
*   透過調整 NCCL 的參數，對長距離 RDMA 通訊進行優化，以減少網路延遲對分散式學習性能的影響。
*   確認了 GPU APN 的可行性，驗證了在分散式資料中心環境下進行大規模 LLM 訓練的可行性。
*   明確 ION APN 的低延遲、高頻寬特性對於大規模 LLM 訓練至關重要。

**4. 時間規劃與里程碑:**

*   2023 年 10 月，發布 GPU APN 的新聞稿。
*   2024 年 3 月，開始提供 ION APN 服務。
*   持續進行 GPU APN 的實證實驗，以驗證其在不同場景下的有效性。
*   將 ION APN 部署到正在建設中的綠色資料中心。

**5. 未解決的技術挑戰:**

*   如何在更複雜的網路拓撲下優化分散式學習的性能。
*   如何自動化 GPU 資源的分配和管理。
*   如何監控和診斷分散式學習任務的性能問題。
*   需要對不同模型的架構進行進一步的調優，以確保在分散式的環境下達到最佳的訓練效果。

**6. 後續行動計畫:**

*   持續驗證 GPU APN 在不同規模和不同模型上的性能表現。
*   將 GPU APN 整合到現有的雲端服務中。
*   撰寫技術文檔，分享 GPU APN 的實施經驗和最佳實踐。
*   評估其他分散式學習框架，如 PyTorch DDP 或 Horovod。
*   與 NVIDIA 合作，進一步優化 Nemo 和 NCCL 在 APN 環境下的性能。
