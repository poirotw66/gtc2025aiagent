# Technical - Intermediate

## Accelerate Reservoir Modeling for the Energy Transition With Physics-Informed AI Techniques

### Key Takeaways

本次會議介紹了如何整合人工智慧來加速地下油藏的建模、優化和管理，這是能源轉型中的一個關鍵挑戰。會議重點介紹了使用序列傅立葉神經算子（Sequential Fourier Neural Operators, SFNO）進行二氧化碳儲存建模，以及使用序列物理資訊神經算子（Sequential Physics-Informed Neural Operators, SPINO）和變分卷積自編碼器（Variational Convolutional Autoencoder, VCAE）進行歷史擬合。
### 重點摘要：
*   利用AI加速油藏建模，應對能源轉型挑戰。
*   使用SFNO模型預測二氧化碳儲存，SPINO和VCAE模型進行歷史擬合。
*   強調了氣候緊急性、數據可用性和AI技術進步是推動該領域發展的三個關鍵因素。
### Topic:
*   AI在能源領域的應用
*   物理資訊機器學習
*   油藏建模與模擬

---

## Profile Large Language Model Trainings on the Grace Hopper Superchip [S72967]

### Key Takeaways

本次會議介紹了 NVIDIA Grace Hopper Superchip 在大型語言模型訓練中的應用，重點介紹了使用 NVIDIA Nsight Systems Profiler 進行性能分析和優化的方法。
### 重點摘要：
*   Grace Hopper Superchip 的架構及其在加速計算和生成式 AI 方面的優勢。
*   NVIDIA Nsight Systems Profiler 的使用，用於識別程式碼中的瓶頸和優化機會。
*   LoRa (Low-Rank Adaptation) 微調大型模型，並使用 Nsight Systems 進行性能分析。
*   通過調整 NumWorkers 參數和使用混合精度訓練等技術來優化訓練工作流程。
### Topic:
*   大型語言模型訓練
*   性能分析與優化
*   Grace Hopper Superchip
*   NVIDIA Nsight Systems

---

## 构建以 Megatron-Core 为核心的大语言模型训练加速生态

### Key Takeaways

本次會議主要介紹了阿里云人工智能平台PAI團隊與英偉達Megatron Core團隊在大語言模型及多模態大模型訓練方面的合作與優化工作。重點介紹了PiMagatron Patch的核心定位與功能，以及在性能優化、功能擴展方面的更新，包括分布式優化器卸載、多模態大模型分布式訓練支持、以及DeepSeek V3相關的訓練實踐。

### Topic:
*   大語言模型訓練
*   多模態大模型訓練
*   性能優化
*   分布式訓練

---

## 大規模言語モデル学習スケールのためのテレコムユースケース [S71554]

### Key Takeaways

本次發表介紹了 NTT Communications 如何利用 GPU over APN 的方法，解決大規模語言模型學習時 GPU 資源不足的問題。透過 NVIDIA 的 NEMO 框架和 Megatron 分散式框架，實現跨數據中心 GPU 資源的有效利用，並透過實證實驗驗證了該方法的可行性。
### 重點摘要：
*   介紹了 GPU over APN 的概念，即透過 APN 網路連接分散的 GPU 資源，以滿足生成 AI 對 GPU 的大量需求。
*   探討了 NVIDIA 的 NEMO 框架和 Megatron 分散式框架，以及它們在分散式學習中的應用。
*   展示了 GPU over APN 的實證實驗結果，驗證了該方法在分散式學習中的有效性。
### Topic: 分散式學習、GPU 資源管理、生成 AI

---

## AI Agents Shaping the Future of Cybersecurity [S72441]

### Key Takeaways

本次會議重點討論了 AI Agent 如何重塑網路安全的未來，涵蓋了從 AI 解決方案到 AI 基礎設施，以及勞動力如何採用 AI 的廣泛視角。講者們分享了各自公司在 AI 應用和網路安全方面的經驗和見解，強調了 AI 在提高效率、檢測威脅和保護數據方面的潛力，同時也指出了與 AI 相關的風險和挑戰。
### 重點摘要：
*   AI 在醫療、金融、交通運輸和聯邦政府等行業的應用日益普及。
*   AI Agent 技術在網路安全領域的應用，例如威脅檢測、漏洞分析和安全自動化。
*   雲安全和 AI 安全之間的相似之處，以及從雲安全中汲取的經驗教訓。
*   數位分身 (Digital Twin) 技術在電網安全中的應用，以及如何利用 AI 增強數位分身的安全性。
*   主權 AI 的概念，以及在資料安全和合規性方面的重要性。
### Topic: AI 安全、網路安全、AI Agent

---

## UFO-Lite：基于自推测解码的低延迟多模态大模型

### Key Takeaways

本次會議主要介紹了百度提出的 UFO Lite，一種針對多模態大模型推理成本和性能的優化方法。該方法基於投機解碼，通過大小模型協同工作，在保證精度的前提下，顯著降低推理延遲。
### 重點摘要：
*   UFO Lite 是業界首個多模態投機解碼工作，解決了多模態投機採樣引入的新挑戰。
*   UFO Lite 適用於任意多模態大模型，可通過自協同進行加速，無需 tokenizer 限制。
*   UFO Lite 基於 Tokenizer 的 LM 進行研發，與緩存機制深度優化，可在 Llama 2 上實現極致推理速度。
*   UFO Lite 通過在線量化和蒸餾等技術，進一步提升加速比和精度。
### Topic: 多模態大模型推理優化、投機解碼、模型加速

---

## 高速・高精度・絶対シミュレーシ

### Key Takeaways

本次會議主要介紹了利用高速、高精度、絕對模擬技術，結合合成數據，在AI藥物發現領域的應用與未來發展。重點在於介紹了アリベクシス公司（Arribexes）的ModBind演算法，以及如何利用該演算法加速和優化藥物發現過程。
### 重點摘要：
*   低分子藥物發現的演進歷程，從偶然發現到基於計算和AI的設計。
*   アリベクシス公司的業務模式：利用模擬和AI技術進行低分子藥物發現，並在臨床前階段授權給製藥公司。
*   ModBind演算法的技術特點：高速、高精度、絕對預測，無需參考化合物。
*   利用ModBind生成的合成數據訓練AI模型，提高AI藥物發現的效率和準確性。
### Topic: AI 藥物發現、分子模擬、合成數據

---

## NVIDIA GPU クラウドを使った API アクセスによる高速アプリ開発 [S73913]

### Key Takeaways

本次會議主要介紹 FPT (FPT Software) 的 AI Platform，特別是 FPT AI Factory，以及如何利用 NVIDIA GPU Cloud 加速 AI 應用開發。會議涵蓋了 FPT 的公司概況、AI 戰略、GPU Cloud 服務、AI Studio、推論服務，以及一系列 AI 產品和解決方案的案例研究。

### 重點摘要：
*   FPT 作為越南最大的數位集團，在全球 30 個國家和地區擁有超過 3 萬名員工。
*   FPT AI Platform 提供 GPU Cloud、AI Studio 和推論服務，支援 AI 模型開發、訓練、部署和應用。
*   FPT AI Factory 提供多種 GPU 資源，包括裸機伺服器、託管 Kubernetes 叢集和 GPU 容器，並提供彈性定價選項。
*   FPT AI Studio 提供 AI 模型微調、模型目錄和 AI Notebook 等功能，簡化 AI 開發流程。
*   FPT 提供一系列 AI 產品和解決方案，包括 IB Chat (企業級生成式 AI 平台) 和 CodeWista (AI 輔助程式碼開發工具)。
*   伊藤忠商事利用 FPT 的 IB Chat 和 CodeWista 實現業務流程轉型，提高生產力和程式碼品質。

### Topic:
*   AI Infrastructure
*   AI Development Platform
*   AI Applications and Solutions

---

## Isaac PerceptorとAutowareを組み合わせたNova Carterの自動運転 [S73870]

### Key Takeaways

本次會議介紹了Tier4公司如何將NVIDIA Isaac Perceptor與Autoware自動駕駛軟體整合到NVIDIA Nova Carter自立移動機器人平台上，並展示了在實際場景中的應用。
### 重點摘要：
*   Tier4公司介紹及其在自動駕駛領域的貢獻，包括開源自動駕駛軟體Autoware。
*   NVIDIA Isaac Perceptor的介紹，特別是其在感知方面的能力，以及如何應用於自立移動機器人。
*   NVIDIA Nova Carter自立移動機器人平台的介紹，包括其硬體配置和軟體支援。
*   Autoware與Nova Carter的整合，展示了在室內環境中，Nova Carter如何使用Autoware進行自主導航和避障。
### Topic: 自動駕駛、機器人、感知、Autoware、Isaac Perceptor、Nova Carter

---

## 使用 NVIDIA 技术为你的母語构建 LLM

### Key Takeaways

本次演講主要探討了如何使用 NVIDIA 技術為資源稀缺語言構建大型語言模型（LLM），重點介紹了使用 NVIDIA Nemo Curator 進行高效數據準備，以及使用 NVIDIA Nemo Framework 進行模型訓練的方法。
### 重點摘要：
*   現有大型語言模型可能不支持某些母語的原因，以及資源稀缺語言構建 LLM 所面臨的挑戰。
*   使用 NVIDIA Nemo Curator 進行高效數據準備的流程，包括數據清洗、詞彙表構建和指令調整數據集創建。
*   使用 NVIDIA Nemo Framework 進行模型訓練的步驟，包括模型選擇、配置、訓練和微調。
*   資源稀缺語言 LLM 的應用案例，例如客服、疫情監控、翻譯和教育等。
*   展望社區合作與未來發展方向，包括支持更多稀缺語言和構建企業級 LLM 訓練平台 VotiMagic。
### Topic: 語言模型、自然語言處理、NVIDIA Nemo Framework、資源稀缺語言

---

## Agentic AI at the Edge Real-Time Sentiment

### Key Takeaways

本次會議主要探討了如何利用代理式AI在邊緣端進行即時情感分析，以提升顧客體驗，特別是在零售環境中。會議展示了Eviden和Infuse合作開發的解決方案，該方案利用現有基礎設施（如監控攝影機）和邊緣運算設備（如NVIDIA Jetson），在保護隱私的前提下，為顧客提供更個性化的服務。
### 重點摘要：
*   代理式AI在零售業的應用，重點在於提升顧客體驗和營收。
*   利用現有基礎設施和邊緣運算，降低部署成本和複雜性。
*   強調隱私保護技術的重要性，確保顧客數據安全。
*   展示了基於NVIDIA Jetson的實時情感分析和廣告投放系統。
### Topic: AI at the Edge, Retail, Customer Experience

---

## 使用 GPU 加速图像视频处理方法的演进

### Key Takeaways

本次會議主要介紹了火山引擎視頻雲如何使用 NVIDIA GPU 加速圖像和視頻處理，涵蓋了 CUDA 加速傳統算法、TensorRT 加速 CNN 模型、GPU 利用率最大化、調度器執行模式以及視覺大模型優化等方面。
### 重點摘要：
*   使用 CUDA 加速傳統圖像處理算法，性能提升顯著。
*   使用 TensorRT 加速 CNN 模型，並通過模型拆分和算子融合等方式優化顯存佔用和性能。
*   通過異步調度提高 GPU 利用率，解決 CPU 前後處理導致的 GPU 閒置問題。
*   採用 GPU 執行器調動模式，解決算法模板數量過多導致的顯存開銷和維護困難問題。
*   針對 LAVA 等視覺大模型進行優化，提升推理速度。
### Topic: GPU 加速、圖像處理、視頻處理、深度學習、TensorRT、CUDA、異步調度、模型優化

---

## RAPIDS in 2025 Accelerated Data Science Everywhere [S73290]

### Key Takeaways

本次會議介紹了 NVIDIA 的 RAPIDS 生態系統在加速資料科學方面的最新進展，涵蓋了資料框架、SQL、機器學習、圖形分析、向量搜尋和大語言模型等領域的開發，以及工具和平台方面的改進，旨在為資料科學家提供更高效、更便捷的加速計算體驗。
### 重點摘要：
*   RAPIDS 生態系統在各個領域的最新進展，包括 pandas、polars、Apache Spark、Scikit-learn、UMAP、HDBSCAN、XGBoost、NetworkX、PyTorch Geometric 等。
*   零程式碼變更加速 (Zero Code Change) 的重要性，讓使用者可以在不修改程式碼的情況下，利用 GPU 加速現有的工作流程。
*   NVIDIA 在開發者體驗方面的努力，包括改進文件、Project Aether、NV Dashboard、統一深度學習和資料科學容器，以及與 Google Colab 和 Snowflake 的合作。
### Topic:
加速資料科學、GPU 計算、機器學習、圖形分析、向量搜尋、大語言模型、開發者工具

---

## Spectrum-X & H200で構築したGPUクラウドサービス開発の最前線

### Key Takeaways

本次會議介紹了 GMO Internet 開發的 GMO GPU Cloud 服務，該服務基於 NVIDIA 的參考架構，專為 AI 模型訓練和機器學習優化。重點介紹了該服務的系統架構、網路配置，以及使用 Spectrum X 實現高效能互連網路的細節。
### 重點摘要：
*   GMO GPU Cloud 服務的介紹，包括其優勢和應用場景。
*   系統架構的詳細說明，包括網路配置、GPU 節點和儲存系統。
*   互連網路的深入探討，重點是 Rail Optimized Topology 和複數控制。
*   構建過程中的經驗分享，包括時間限制、合作夥伴關係和 NVIDIA 的支援。
*   服務的效能指標，包括在 Top500 超級電腦排行榜上的排名。
### Topic: GPU 雲服務、高效能網路、AI 基礎設施

---

## Diffusion Models The Swiss Army Knife for Generative AI in Science 

### Key Takeaways

本次會議主要介紹了擴散模型在科學領域的應用，包括天氣預測、蛋白質和小型分子生成等。講者分享了團隊在過去一年中構建的四個用例，並總結了在科學應用中構建生成模型時的經驗教訓和解決方案。
### 重點摘要：
*   擴散模型和流模型的基本原理和數學描述。
*   擴散模型在天氣預測、重尾數據生成、蛋白質和小型分子生成等科學領域的應用案例。
*   構建科學領域生成模型時的關鍵設計決策，包括訓練數據品質、數據表示、網路架構、損失函數、採樣方法和評估指標。
### Topic: 生成式AI、擴散模型、科學應用

---

