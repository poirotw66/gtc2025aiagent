# 大規模言語モデル学習スケールのためのテレコムユースケース [S71554]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E5%A4%A7%E8%A6%8F%E6%A8%A1%E8%A8%80%E8%AA%9E%E3%83%A2%E3%83%86%E3%82%99%E3%83%AB%E5%AD%A6%E7%BF%92%E3%82%B9%E3%82%B1%E3%83%BC%E3%83%AB%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%83%86%E3%83%AC%E3%82%B3%E3%83%A0%E3%83%A6%E3%83%BC%E3%82%B9%E3%82%B1%E3%83%BC%E3%82%B9%20%5BS71554%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1726042111947001pTvu)
# 大規模語言模型學習規模的電信使用案例 [S71554]

## Key Takeaways
本次發表介紹了 NTT Communications 如何利用 GPU over APN 的方法，解決大規模語言模型學習時 GPU 資源不足的問題。透過 NVIDIA 的 NEMO 框架和 Megatron 分散式框架，實現跨數據中心 GPU 資源的有效利用，並透過實證實驗驗證了該方法的可行性。
### 重點摘要：
*   介紹了 GPU over APN 的概念，即透過 APN 網路連接分散的 GPU 資源，以滿足生成 AI 對 GPU 的大量需求。
*   探討了 NVIDIA 的 NEMO 框架和 Megatron 分散式框架，以及它們在分散式學習中的應用。
*   展示了 GPU over APN 的實證實驗結果，驗證了該方法在分散式學習中的有效性。
### Topic: 分散式學習、GPU 資源管理、生成 AI

## 會議主題
會議主要探討了如何利用電信網路（APN）連接分散的 GPU 資源，以解決大規模語言模型學習時 GPU 資源不足的問題。會議重點在於介紹 GPU over APN 的概念，以及如何透過 NVIDIA 的 NEMO 框架和 Megatron 分散式框架實現跨數據中心 GPU 資源的有效利用。

## 主要技術點
*   **GPU over APN：** 一種利用 APN 網路連接分散的 GPU 資源，以滿足生成 AI 對 GPU 大量需求的解決方案。
*   **NVIDIA NEMO 框架：** 一個用於構建和訓練對話式 AI 模型的工具包，支援多種模型架構和分散式學習。
*   **Megatron 分散式框架：** 一個用於訓練大型語言模型的分散式框架，支援多種並行策略，如數據並行、模型並行和流水線並行。
*   **IoN APN：** NTT 集團提供的高容量、高品質、低延遲、低功耗的網路服務，用於連接分散的 GPU 資源。
*   **GPU Direct RDMA：** 一種允許 GPU 直接訪問遠端記憶體的技術，可以減少 CPU 的參與，提高通信效率。
*   **NCCL (NVIDIA Collective Communications Library)：** NVIDIA 的集合通信庫，用於實現多 GPU 之間的快速通信。
*   **分散式學習框架的選擇：** 根據實際需求選擇合適的分散式學習框架，如 NEMO 或 Megatron。
*   **長距離通信延遲的解決方案：** 透過調整 NCCL 的參數，如 buffer size 和 QP size，來優化長距離 RDMA 的性能。

## 決策與共識
*   採用 GPU over APN 的方法，解決大規模語言模型學習時 GPU 資源不足的問題。
*   利用 NVIDIA 的 NEMO 框架和 Megatron 分散式框架，實現跨數據中心 GPU 資源的有效利用。
*   透過 IoN APN 網路連接分散的 GPU 資源，提供高容量、高品質、低延遲的通信。
*   透過調整 NCCL 的參數，優化長距離 RDMA 的性能。

## 時間規劃與里程碑
*   已於去年 10 月發布 GPU over APN 的新聞稿。
*   已於去年 3 月開始提供 IoN APN 服務。
*   正在建設 Green Next Center 數據中心，並透過 IoN APN 連接各數據中心。
*   持續進行 GPU over APN 的實證實驗，驗證該方法的可行性和有效性。

## 未解決的技術挑戰
*   如何選擇合適的分散式學習框架，以適應不同的模型架構和數據規模。
*   如何優化長距離通信延遲，以提高分散式學習的效率。
*   如何將 GPU over APN 應用於更多領域，如醫療、金融等。

## 後續行動計劃
*   繼續進行 GPU over APN 的實證實驗，驗證該方法在不同場景下的有效性。
*   與 NVIDIA 合作，優化 NEMO 框架和 Megatron 分散式框架，以提高分散式學習的效率。
*   擴大 IoN APN 網路的覆蓋範圍，提供更多高容量、高品質、低延遲的通信服務。
*   探索 GPU over APN 在更多領域的應用，推動 AI 技術的發展。
