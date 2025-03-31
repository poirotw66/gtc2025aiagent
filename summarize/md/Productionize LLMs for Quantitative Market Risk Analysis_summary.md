# Productionize LLMs for Quantitative Market Risk Analysis
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Productionize%20LLMs%20for%20Quantitative%20Market%20Risk%20Analysis&tab.catalogallsessionstab=16566177511100015Kus#/session/1732702263904001YvIf)
# 將 LLM 產品化以進行市場風險量化分析

## Key Takeaways
本次會議主要探討了如何將大型語言模型（LLMs）應用於市場風險的量化分析，重點介紹了在 Barclays 銀行進行的探索性分析，以及如何利用 NVIDIA 的技術棧來實現 LLM 的產品化。
### 重點摘要：
*   利用 LLMs 和 RAG（Retrieval Augmented Generation）技術，從大量非結構化數據中提取有價值的資訊，以應對市場風險分析中數據過載、缺乏即時分析和主觀性等挑戰。
*   強調在內部部署 GPU 生態系統中最大化 GPU 利用率的重要性，並提出了一種基於 Kubernetes 的可擴展架構，以支持不同類型的工作負載。
*   展示了 NVIDIA 的 NEMO 框架在查詢和檢索方面的應用，並通過基準測試比較了不同 LLM 框架的性能，包括 tokens per second 和 time to first token。
### Topic: LLMs, Market Risk Analysis, NVIDIA NEMO, GPU Utilization

## 會議主題
會議主要探討了如何利用 LLMs 和 NVIDIA 的軟硬體框架，在內部環境中構建一個可擴展、高效的市場風險量化分析平台。重點關注 GPU 的最大化利用、工作負載的容器化和自動擴展，以及監控和預測潛在問題。

## 主要技術點
*   **GPU 最大化利用：** 強調在數據準備、模型訓練、微調、部署、推理、監控、可解釋性和安全控制等各個階段最大化 GPU 的利用率。
*   **GPU 隔離：** 討論了如何在同一 GPU 上運行多個團隊的不同類型工作負載（例如，傳統 ML 模型和 GenAI 模型），以提高資源利用率。
*   **容器化和 Kubernetes：** 強調所有解決方案都應完全容器化並與 Kubernetes 兼容，以便於部署和管理。
*   **NVIDIA NEMO 框架：** 展示了 NEMO 框架在查詢和檢索方面的應用，以及如何使用 Colang 語言進行配置。
*   **RAG（Retrieval Augmented Generation）：** 討論了 RAG 技術如何利用即時市場數據，而不是僅依賴預訓練知識，從而提高 LLM 的準確性。
*   **基準測試：** 通過基準測試比較了不同 LLM 框架（例如，NEMO、VLLM、Ollama、TGI）在 tokens per second 和 time to first token 方面的性能。
*   **監控和自動擴展：** 強調了監控 GPU、Kubernetes 和存儲的重要性，並討論了如何使用 Prometheus 和 Grafana 進行監控，以及如何基於指標自動擴展工作負載。

## 決策與共識
*   在內部部署 GPU 生態系統中構建市場風險量化分析平台。
*   最大化 GPU 利用率，並採用容器化和 Kubernetes 來實現可擴展性和靈活性。
*   使用 NVIDIA NEMO 框架進行查詢和檢索。
*   實施 robust 的監控和自動擴展機制。

## 時間規劃與里程碑
會議中未明確提及具體的時間規劃與里程碑，但強調了持續實驗、基準測試和優化的重要性。

## 未解決的技術挑戰
*   如何進一步提高 LLM 在市場風險分析中的準確性和可靠性。
*   如何有效地管理和監控大規模 GPU 集群。
*   如何解決與數據隱私和安全相關的問題。

## 後續行動計劃
*   繼續實驗和基準測試不同的 LLM 框架和技術。
*   優化 GPU 利用率和工作負載的自動擴展。
*   開發 robust 的監控和預測機制。
*   探索將 LLM 應用於更多市場風險分析場景。
