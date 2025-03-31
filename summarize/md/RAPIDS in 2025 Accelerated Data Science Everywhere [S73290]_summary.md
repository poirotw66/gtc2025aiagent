# RAPIDS in 2025 Accelerated Data Science Everywhere [S73290]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=RAPIDS%20in%202025%20Accelerated%20Data%20Science%20Everywhere%20%5BS73290%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1728323939538001F71p)
# RAPIDS 在 2025 年：加速資料科學無所不在 [S73290]

## Key Takeaways
本次會議介紹了 NVIDIA 的 RAPIDS 生態系統在加速資料科學方面的最新進展，涵蓋了資料框架、SQL、機器學習、圖形分析、向量搜尋和大語言模型等領域的開發，以及工具和平台方面的改進，旨在為資料科學家提供更高效、更便捷的加速計算體驗。
### 重點摘要：
*   RAPIDS 生態系統在各個領域的最新進展，包括 pandas、polars、Apache Spark、Scikit-learn、UMAP、HDBSCAN、XGBoost、NetworkX、PyTorch Geometric 等。
*   零程式碼變更加速 (Zero Code Change) 的重要性，讓使用者可以在不修改程式碼的情況下，利用 GPU 加速現有的工作流程。
*   NVIDIA 在開發者體驗方面的努力，包括改進文件、Project Aether、NV Dashboard、統一深度學習和資料科學容器，以及與 Google Colab 和 Snowflake 的合作。
### Topic:
加速資料科學、GPU 計算、機器學習、圖形分析、向量搜尋、大語言模型、開發者工具

## 會議主題
會議主要探討了 NVIDIA RAPIDS 生態系統如何透過 GPU 加速，提升資料科學工作流程的效能，並介紹了在資料框架、機器學習、圖形分析和向量搜尋等領域的最新技術發展。

## 主要技術點
*   **GPU 加速資料框架：**
    *   **pandas 和 polars：** 透過 QDF 基礎函式庫，實現零程式碼變更的 GPU 加速，效能提升高達 50 倍和 13 倍。
    *   **Unified Memory：** 允許使用超過 GPU 記憶體限制的資料集，即使在較小的 GPU 上也能處理大型資料。
    *   **Remote I/O 優化：** 針對 Amazon S3 等遠端儲存平台進行優化，提升分散式資料框架分析的效能。
*   **Apache Spark 加速：**
    *   **RAPIDS Accelerator for Apache Spark：** 零程式碼變更加速，降低成本、節省能源，並縮短價值實現時間。
    *   **NVIDIA Decision Support Benchmark：** 顯示在 CPU Spark 上執行 100 個 SQL 查詢需要 6 倍的時間，並可節省高達 80% 的成本。
*   **機器學習加速：**
    *   **QML：** 透過零程式碼變更加速 Scikit-learn、UMAP 和 HDBSCAN，效能提升 5 到 200 倍。
    *   **XGBoost 3.0：** 重新設計的外部記憶體介面，允許在單個 Grace Hopper 系統上訓練高達 1TB 或更大的資料集。
    *   **Forest Inference Library (FIL)：** 加速樹模型的推論，效能提升高達 4 倍，並提供新的 CPU 執行模式和自動優化功能。
*   **圖形分析加速：**
    *   **NetworkX：** 透過 Coup Graph 實現加速，效能提升高達 600 倍。
    *   **PyTorch Geometric：** 透過 KooGraph 和 WholeGraph 實現加速，在大型圖形上進行端到端訓練工作流程時，效能提升高達 3 倍。
*   **向量搜尋和 LLM 工作流程：**
    *   **Nemo Curator：** 可擴展、可配置的工具組，用於處理資料以訓練大型語言模型和 AI 模型。
    *   **KUVS：** 加速向量搜尋索引建立和實際搜尋，與 Milvus、Weviate 和 OpenSearch 等向量資料庫合作。

## 決策與共識
*   強調零程式碼變更加速的重要性，讓使用者可以輕鬆地利用 GPU 加速現有的工作流程。
*   強調 RAPIDS 生態系統與其他工具和平台的整合，例如 Apache Spark、Scikit-learn、PyTorch Geometric、Google Colab 和 Snowflake。
*   強調 NVIDIA 在開發者體驗方面的努力，包括改進文件、Project Aether 和 NV Dashboard。

## 時間規劃與里程碑
*   XGBoost 3.0 的發布候選版本現已可用，正式版本即將發布。
*   新的 Forest Inference Library (FIL) 的實驗性版本可在 nightly packages 中使用，穩定版本即將發布。
*   Project Aether 已宣布，NVIDIA 正在尋找有興趣早期訪問的使用者。
*   Snowflake Notebooks 中加速資料科學現已公開預覽。

## 未解決的技術挑戰
*   如何進一步優化 GPU 加速的效能，特別是在處理大型資料集和複雜模型時。
*   如何簡化 GPU 加速的部署和管理，讓更多使用者可以輕鬆地利用 GPU 的強大功能。
*   如何擴展 RAPIDS 生態系統，以支援更多領域和應用，例如自然語言處理、電腦視覺和科學計算。

## 後續行動計劃
*   繼續開發和優化 RAPIDS 生態系統中的各個函式庫和工具。
*   與社群合作，擴展 RAPIDS 生態系統，並支援更多領域和應用。
*   提供更多資源和支援，幫助使用者學習和使用 RAPIDS 生態系統。
*   與 Google Colab 和 Snowflake 等平台合作，將加速資料科學帶給更多使用者。
