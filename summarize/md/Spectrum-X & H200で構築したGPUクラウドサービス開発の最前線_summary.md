# Spectrum-X & H200で構築したGPUクラウドサービス開発の最前線
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Spectrum-X%20%26%20H200%E3%81%A6%E3%82%99%E6%A7%8B%E7%AF%89%E3%81%97%E3%81%9FGPU%E3%82%AF%E3%83%A9%E3%82%A6%E3%83%88%E3%82%99%E3%82%B5%E3%83%BC%E3%83%92%E3%82%99%E3%82%B9%E9%96%8B%E7%99%BA%E3%81%AE%E6%9C%80%E5%89%8D%E7%B7%9A&tab.catalogallsessionstab=16566177511100015Kus#/session/1733447858525001uBOk)
# Spectrum-X & H200 構建的 GPU 雲服務開發最前線

## Key Takeaways
本次會議介紹了 GMO Internet 開發的 GMO GPU Cloud 服務，該服務基於 NVIDIA 的參考架構，專為 AI 模型訓練和機器學習優化。重點介紹了該服務的系統架構、網路配置，以及使用 Spectrum X 實現高效能互連網路的細節。
### 重點摘要：
*   GMO GPU Cloud 服務的介紹，包括其優勢和應用場景。
*   系統架構的詳細說明，包括網路配置、GPU 節點和儲存系統。
*   互連網路的深入探討，重點是 Rail Optimized Topology 和複數控制。
*   構建過程中的經驗分享，包括時間限制、合作夥伴關係和 NVIDIA 的支援。
*   服務的效能指標，包括在 Top500 超級電腦排行榜上的排名。
### Topic: GPU 雲服務、高效能網路、AI 基礎設施

## 會議主題
會議主要探討了 GMO Internet 如何利用 NVIDIA 的 Spectrum X 和 H200 GPU 構建高效能 GPU 雲服務，重點介紹了網路架構的設計和優化，以及在短時間內成功部署服務的經驗。

## 主要技術點
*   **NVIDIA H200 GPU：** 採用 NVIDIA H200 GPU，提供強大的計算能力，適用於 AI 模型訓練和機器學習。
*   **NVIDIA Spectrum X：** 使用 NVIDIA Spectrum X 網路解決方案，包括交換機和 Bluefield 3 SuperNIC，實現低延遲、高頻寬的互連網路。
*   **Rail Optimized Topology：** 採用 Rail Optimized Topology，確保每個 GPU 都有足夠的頻寬，最大化 GPU 的效能。
*   **複數控制：** 實施複數控制機制，包括 RoCEv2 和 NVIDIA 獨有的複數控制，避免網路擁塞和封包遺失，確保網路的穩定性和可靠性。
*   **Bluefield 3 SuperNIC：** 使用 Bluefield 3 SuperNIC，實現可程式化的網路處理，並與 Spectrum 交換機協同工作，提供高效能的網路服務。
*   **DDN ES400NVX2 儲存：** 採用 DDN ES400NVX2 儲存系統，提供高速的資料讀寫能力，滿足 GPU 計算的需求。
*   **SLAM 任務管理系統：** 使用 SLAM 任務管理系統，簡化任務提交和管理，提高 GPU 資源的利用率。

## 決策與共識
*   採用 NVIDIA 的參考架構和 Spectrum X 網路解決方案，以實現高效能的 GPU 雲服務。
*   與 NVIDIA 和其他合作夥伴密切合作，以加快服務的部署速度。
*   重視網路的穩定性和可靠性，實施複數控制機制，確保 GPU 計算的效能。

## 時間規劃與里程碑
*   在短時間內完成 GPU 雲服務的部署，並在 Top500 超級電腦排行榜上取得優異成績。
*   持續優化服務的效能和功能，以滿足不斷變化的客戶需求。
*   計劃擴展服務的規模，增加更多的 GPU 資源。

## 未解決的技術挑戰
*   Bluefield 3 SuperNIC 的設定初始化問題，需要透過自動化腳本解決。
*   Spectrum 交換機的 Cumulus Linux 作業系統，需要熟悉 NV 命令和 Linux 命令。
*   傳統資料中心的電力和散熱限制，需要仔細規劃機櫃的配置和纜線的佈線。

## 後續行動計劃
*   繼續優化 Bluefield 3 SuperNIC 的設定管理，提高系統的穩定性。
*   深入研究 Cumulus Linux 作業系統，提高網路管理的效率。
*   探索更高效的散熱方案，以提高 GPU 資源的密度。
*   推廣 GMO GPU Cloud 服務，吸引更多的客戶。
