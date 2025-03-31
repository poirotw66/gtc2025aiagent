# NVIDIA NIM_NeMoで実現する生成AIによる資産運用レポーティングの変革 [S73894]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=NVIDIA%20NIM_NeMo%E3%81%A6%E3%82%99%E5%AE%9F%E7%8F%BE%E3%81%99%E3%82%8B%E7%94%9F%E6%88%90AI%E3%81%AB%E3%82%88%E3%82%8B%E8%B3%87%E7%94%A3%E9%81%8B%E7%94%A8%E3%83%AC%E3%83%9B%E3%82%9A%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%AF%E3%82%99%E3%81%AE%E5%A4%89%E9%9D%A9%20%5BS73894%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1733484884857001LNSv)
# NVIDIA NIM_NeMo實現的生成AI在資產運用報告中的變革 [S73894]

## Key Takeaways
本次簡報介紹了如何利用 NVIDIA 的 NIM 和 NeMo 框架，變革資產運用報告業務。分享了企業界，特別是資產運用領域中生成 AI 應用的具體案例，以及從中獲得的知識。
### 重點摘要：
*   利用 NVIDIA 的 NIM 和 NeMo 框架，變革資產運用報告業務。
*   探討了開放原始碼 LLM 在模型風險管理（MRM）原則上的優勢，以及客製化的靈活性。
*   比較了 NVIDIA NIMO 和 Hugging Face 在學習速度和推論速度上的差異，並說明了選擇 NIMO 的原因。
*   介紹了使用 NVIDIA Inference Microservice (NIMO) 實作推論引擎，以及社內應用程式的運作方式。
### Topic: 生成式 AI、資產運用、NVIDIA NIM、NVIDIA NeMo、LLM 客製化

## 會議主題
會議主要探討了如何利用 NVIDIA 的 NIM 和 NeMo 框架，以及開放原始碼 LLM，來優化資產運用報告流程，特別是月度報告的評論撰寫。重點在於提高效率、確保一致性，並促進知識共享。

## 主要技術點
*   **開放原始碼 LLM 的選擇：** 基於模型風險管理（MRM）原則、客製化彈性、以及資料安全性的考量，選擇開放原始碼 LLM。
*   **模型客製化：** 使用 LoRA 和 SFT（Supervised Fine-Tuning）等技術，對 LLM 進行微調，以符合特定的報告需求。
*   **NVIDIA NIMO 的應用：** 利用 NIMO 簡化 LLM 的微調，並加速學習和推論過程。
*   **推論引擎實作：** 使用 NVIDIA Inference Microservice (NIMO) 實作推論引擎，提高吞吐量。
*   **社內應用程式開發：** 使用 Python、Streamlit 和 LangChain 開發社內應用程式，方便使用者輸入評論草稿，並利用 LLM 進行修改和完善。

## 決策與共識
*   基於模型風險管理、客製化彈性和資料安全性的考量，選擇開放原始碼 LLM。
*   採用 NVIDIA NIMO 作為 LLM 開發和部署的平台，以提高效率和可靠性。
*   開發社內應用程式，以方便使用者利用 LLM 進行報告評論的撰寫和修改。

## 時間規劃與里程碑
*   初期驗證階段採用 LoRA 進行微調。
*   後續階段採用 SFT 進行更精確的微調。
*   開發社內應用程式並進行測試。
*   將 LLM 應用於其他業務領域。

## 未解決的技術挑戰
*   如何進一步提高 LLM 的準確性和可靠性，減少幻覺現象。
*   如何有效地管理和利用大量的金融資料，以訓練更專業的 LLM。
*   如何將 LLM 應用於更多不同的資產運用業務。

## 後續行動計劃
*   擴大 LLM 的應用範圍，包括新聞文本分析和金融專業文檔分析。
*   開發公司獨有的領域特定 LLM，以涵蓋更廣泛的資產運用業務。
*   持續優化模型，並將其應用於實際的報告流程中。
