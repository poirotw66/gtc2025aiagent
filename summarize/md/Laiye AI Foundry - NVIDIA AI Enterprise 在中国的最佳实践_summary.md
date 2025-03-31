# Laiye AI Foundry - NVIDIA AI Enterprise 在中国的最佳实践
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Laiye%20AI%20Foundry%20-%20NVIDIA%20AI%20Enterprise%20%E5%9C%A8%E4%B8%AD%E5%9B%BD%E7%9A%84%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5&tab.catalogallsessionstab=16566177511100015Kus#/session/1726190594557001j0HX)
# Laiye AI Foundry - NVIDIA AI Enterprise 在中國的最佳實踐

## Key Takeaways
本次會議由 LINEA 科技分享 LINEA AI 工廠如何利用 NVIDIA AI Enterprise 在中國實現最佳實踐。LINEA 科技致力於為企業提供從數據到智能決策的一站式平台，幫助企業高效利用主權數據，通過低成本的大模型訓練和微調實現智能化轉型。
### 重點摘要：
*   LINEA AI 工廠的總覽與架構，包括基礎設施層、模型生產服務、模型應用層和用戶服務層。
*   LINEA AI 工廠的管理平台，專為高效管理和優化大規模 GPU 集群而設計。
*   LINEA AI 工廠提供的數據服務、大模型微調和定制服務、模型推理服務、知識庫服務以及模型安全服務。
*   LINEA AI 工廠在實際案例中的應用，包括大健康諮詢業務和金融欺詐交易檢測場景。
### Topic: AI 工廠、NVIDIA AI Enterprise、大模型、微調、推理、知識庫、安全服務

## 會議主題
會議主要探討了 LINEA AI 工廠如何基於 NVIDIA AI Enterprise，構建高效、可靠且靈活的生成式 AI 開發平台，並提供全方位的服務，助力企業以低成本實現數據驅動的智能決策。

## 主要技術點
*   **GPU 集群管理：** 基於 NVIDIA AI Enterprise 中的 BCM 集群管理組件，實現萬卡規模 GPU 集群的統一管理、動態部署擴展以及高性能的多用戶多租戶隔離。
*   **全棧優化：** 對計算網絡、GPU 的計算網絡、存儲網絡的通信帶寬和延時進行一系列優化，提升模型利用率 MFU，增強模型生產能力。
*   **模型生產服務：** 涵蓋數據預處理、模型預訓練、模型對齊、模型微調等關鍵環節，廣泛採用 NVIDIA AI Enterprise 中的 NEMO Crate、NEMO MicroTrain、NEMO Framework 和 NEMO Guardrails 等組件。
*   **模型推理服務：** 融合 NVIDIA AI Enterprise 的 NEMO 技術，結合 LINEA 的深度優化，推出 LINEA 大模型 Inference Micro Service，提供高效穩定的 Token API 服務。
*   **數據服務：** 使用 NVIDIA AI Enterprise 的數據處理組件，包括 MVingest 和 NEMO DataCrate，簡化數據處理流程，提升數據質量。
*   **模型微調和定制服務：** 基於 LINEA AI 工廠的強大數據服務，提供多種先進的增強方法，包括 ISTU 和 SPC，為模型定制優化提供全方位的支持。
*   **高性能訓練框架：** 基於 NVIDIA AI Enterprise 中的 NEMO MicroTrain 訓練框架進行深度優化，提升在多卡機訓中的模型訓練效率。
*   **知識庫服務：** 基於 Hybrid 的 RAG 方案，融合 GraphRAG 和 VectorRAG 的優勢，並借助 NEMO 的模型，顯著提升檢索的準確度和速度。
*   **大模型安全服務：** 使用 NEMO Guardrails 的安全護欄組件，協助客戶高效地完成政策法規所需要的大模型備案服務。

## 決策與共識
*   基於 NVIDIA AI Enterprise 構建 LINEA AI 工廠，提供高效、可靠且靈活的生成式 AI 開發平台。
*   採用全棧優化方案，提升模型利用率和生產能力。
*   融合 NVIDIA AI Enterprise 的 NEMO 技術，結合 LINEA 的深度優化，提供高效穩定的模型推理服務。
*   使用 NVIDIA AI Enterprise 的數據處理組件，簡化數據處理流程，提升數據質量。
*   提供多種先進的增強方法，為模型定制優化提供全方位的支持。
*   基於 Hybrid 的 RAG 方案，融合 GraphRAG 和 VectorRAG 的優勢，並借助 NEMO 的模型，顯著提升檢索的準確度和速度。
*   使用 NEMO Guardrails 的安全護欄組件，協助客戶高效地完成政策法規所需要的大模型備案服務。

## 時間規劃與里程碑
*   持續優化 LINEA AI 工廠的各項服務和功能。
*   擴大 LINEA AI 工廠在各行業的應用。
*   與 NVIDIA 保持緊密合作，共同推動 AI 技術的發展。

## 未解決的技術挑戰
*   如何進一步提升模型訓練和推理的效率。
*   如何更好地解決大模型安全和合規問題。
*   如何將 LINEA AI 工廠應用於更多垂直領域。

## 後續行動計劃
*   繼續優化 LINEA AI 工廠的各項服務和功能。
*   加強與 NVIDIA 的合作，共同開發新的 AI 技術。
*   擴大 LINEA AI 工廠在各行業的應用，助力企業實現智能化轉型。
