# NVIDIA 革新智能座舱技术发展
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=NVIDIA%20%E9%9D%A9%E6%96%B0%E6%99%BA%E8%83%BD%E5%BA%A7%E8%88%B1%E6%8A%80%E6%9C%AF%E5%8F%91%E5%B1%95&tab.catalogallsessionstab=16566177511100015Kus#/session/1736180037091001qbos)
# NVIDIA 革新智能座艙技術發展

## Key Takeaways
本次會議主要介紹了NVIDIA在生成式AI應用於智能座艙，以及數據中心與車端大模型推理優化加速的解決方案。涵蓋了全鏈路加速、大模型推理框架TRT-LM，以及端側部署等關鍵技術。
### 重點摘要：
*   NVIDIA NEMO平台：端到端的全流程生成式AI解決方案，涵蓋數據處理、分布式訓練、模型客製化、推理加速、RAG以及安全護欄等階段。
*   Curator數據處理Pipeline：包含文本、圖片和視頻預處理，利用Rapids等組件加速數據清洗、去重和過濾。
*   FP8訓練：利用Transformer Engine庫，通過E4M3和E5M2格式，在計算密集型算子上提供更高的算力，並節省顯存。
*   TRT-LM：針對數據中心大模型推理的加速框架，提供高效Runtime、深度優化Kernel、多模型支持、自定義Workflow和高級量化方法。
*   DriveOS LLM SDK (DriveLM)：專為車端量身定制的大模型推理框架，提供優化加速kernel、輕量化推理Runtime和主流模型端到端推理。
### Topic:
*   生成式AI應用
*   大模型推理優化
*   端側部署

## 會議主題
會議主要探討了NVIDIA在智能座艙中應用生成式AI的技術，以及在數據中心和車端針對大模型推理的優化加速方案。重點介紹了NEMO平台、Curator數據處理Pipeline、FP8訓練、TRT-LM框架和DriveOS LLM SDK等關鍵技術。

## 主要技術點
*   **NEMO平台：** 提供端到端的全流程解決方案，涵蓋數據處理、分布式訓練、模型客製化、推理加速、RAG以及安全護欄等階段，並集成業界高效的優化點。
*   **Curator：** 數據處理Pipeline，包含文本、圖片和視頻預處理，利用Rapids等組件加速數據清洗、去重和過濾，形成高質量數據集。
*   **FP8訓練：** 利用Transformer Engine庫，通過E4M3和E5M2格式，在計算密集型算子上提供更高的算力，並節省顯存。通過Tensor Scaling和Delay Scaling等技術解決精度挑戰。
*   **TRT-LM：** 針對數據中心大模型推理的加速框架，提供高效Runtime（Batch Scheduler、KVcache設計、顯存管理）、深度優化Kernel（Attention、矩陣層）、多模型支持（Decoder Only、Encoder Decoder、多模態）、自定義Workflow（Multi-Lora、Logic Processing）和高級量化方法（FP8、FP4、SmoothQuant）。
*   **多模態大模型部署：** 以千問VL為例，將視覺編碼器和語言模型主體部分分離部署，靈活調整分布式並行設置，並利用TRT-LM的Kernel優化、Runtime優化和模型量化等技術加速推理。
*   **DIT模型優化：** 採用TP（張量並行）和CP（序列並行）等分布式並行策略，並使用FP8量化進一步加速推理。
*   **DriveOS LLM SDK (DriveLM)：** 專為車端量身定制的大模型推理框架，基於C++開發，滿足車規功能安全要求，提供優化加速kernel、輕量化推理Runtime和主流模型端到端推理。支持INT4、NVFP4、FP8和FP16等多種推理精度。
*   **NVFP4精度格式：** NVIDIA定義的E2M1的FP4精度格式，採用W4A4的量化和計算方式，通過動態PerBlock量化和靜態二次量化等技術提高精度，並利用TensorCore硬件加速指令提升性能。

## 決策與共識
*   在智能座艙中廣泛應用生成式AI，提升用戶體驗和自動駕駛決策能力。
*   採用NEMO平台構建生成式AI應用，利用Curator進行數據預處理，並使用FP8訓練加速模型訓練。
*   在數據中心使用TRT-LM框架加速大模型推理，並根據具體模型和場景選擇合適的優化策略。
*   在車端使用DriveOS LLM SDK部署大模型，並根據性能和精度需求選擇合適的推理精度，如NVFP4。

## 時間規劃與里程碑
*   持續迭代NEMO平台，集成更多高效的優化點。
*   不斷完善TRT-LM框架，支持更多模型和自定義Workflow。
*   持續優化DriveOS LLM SDK，提高性能和易用性，並集成到DriveOS中。
*   推廣NVFP4精度格式，並在硬件和軟件層面提供更好的支持。

## 未解決的技術挑戰
*   IP8訓練對精度帶來的挑戰，需要通過混合精度訓練等技術來解決。
*   端側大模型推理的性能和功耗平衡，需要在硬件和軟件層面進行持續優化。
*   INT4的prefuel階段性能仍有提升空間，需要進一步優化。

## 後續行動計劃
*   繼續開發和優化NEMO平台、TRT-LM框架和DriveOS LLM SDK。
*   研究和推廣NVFP4精度格式，並在硬件和軟件層面提供更好的支持。
*   針對車端常用模型和配置進行專門優化，提高推理性能。
*   持續完善參考模型文檔和核心功能模塊，提高工具鏈對於新模型的適配度和靈活性。
