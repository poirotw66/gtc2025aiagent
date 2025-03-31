# 効率的なソブリンAIの最前線：データセンターからAIアプリケーションまで [S73917]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E5%8A%B9%E7%8E%87%E7%9A%84%E3%81%AA%E3%82%BD%E3%83%95%E3%82%99%E3%83%AA%E3%83%B3AI%E3%81%AE%E6%9C%80%E5%89%8D%E7%B7%9A%EF%BC%9A%E3%83%86%E3%82%99%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%B3%E3%82%BF%E3%83%BC%E3%81%8B%E3%82%89AI%E3%82%A2%E3%83%95%E3%82%9A%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%BE%E3%81%A7%E3%82%99%20%5BS73917%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1733747594330001Diny)
# 高效率主權AI的最前線：從數據中心到AI應用 [S73917]

## Key Takeaways
本次演講主要介紹了Kindle Japan在實現主權AI（Sovereign AI）時面臨的挑戰，並分享了Kindle Japan Private Cloud AI Services的實踐案例，該服務利用Dell AI Factory with NVIDIA來支持客戶生成AI應用程式的實施和導入。
### 重點摘要：
*   主權AI的定義與重要性：強調在數據治理、合規性、數據主權和保護業務數據的同時，利用AI提升競爭優勢。
*   Kindle Japan Private Cloud AI Services：介紹了該服務的四個主要組成部分，包括實體環境（Kindle Vital AI Lab Service）、AI應用程式開發支援、AI基礎設施的設計與實施，以及應用程式和基礎設施的運營服務。
*   數據中心設計考量：強調了在高密度GPU環境下，數據中心在電力、散熱、噪音控制和節能方面的設計要點。
*   AI基礎設施堆疊：介紹了從數據中心到AI應用程式的技術堆疊，包括基礎設施、AI平台、AI框架和應用程式層。
### Topic: AI Infrastructure, Sovereign AI, Private Cloud

## 會議主題
會議主要探討了在構建主權AI時，如何從數據中心到AI應用程式的各個層面進行設計和實施，以應對數據治理、合規性、數據主權和業務數據保護等挑戰，同時實現高效的AI應用。

## 主要技術點
*   **數據中心設計：**
    *   高密度GPU環境下的電力和散熱管理，包括空調模擬、風量強化和熱通道設計。
    *   噪音控制，包括使用耳機和隔音屏障。
    *   節能措施，包括氣流管理和可再生能源利用。
*   **AI基礎設施：**
    *   超高速、低延遲網路，使用RoCE（RDMA over Converged Ethernet）技術。
    *   高速儲存，支持RDMA和GPU Direct Storage。
    *   可擴展的伺服器架構，支持GPU變更和節點添加。
*   **數據治理和AI工作流程：**
    *   利用NVIDIA AI Enterprise功能，確保數據品質和可觀測性。
    *   數據生命週期管理，包括數據收集、轉換、儲存、查詢和響應生成。
*   **運營自動化和效率：**
    *   端到端自動化和自助服務，減少運營負擔。
    *   使用NIMO GPU Operator、Kubernetes和Base Command Manager進行協調。
    *   使用Prometheus和Grafana進行監控，並與ITSM工具集成。
*   **安全考量：**
    *   基於責任共擔模型，從使用者和基礎設施提供者的角度設計安全性。
    *   參考雲端控制矩陣（Cloud Control Matrix）框架，確保符合法規和指南。
*   **治理和合規性：**
    *   基於Kindril的責任AI指南，對AI平台和工作負載進行全面評估。
    *   建立跨部門流程，明確AI和數據的責任歸屬。
    *   使用NVIDIA AI Enterprise組件，實現數據和AI的治理。

## 決策與共識
*   主權AI對於保護數據、確保合規性和提升競爭優勢至關重要。
*   構建主權AI需要從數據中心到AI應用程式的全面考量。
*   利用現有技術和框架，如NVIDIA AI Enterprise，可以簡化主權AI的實施。
*   安全性和治理是主權AI的關鍵組成部分，需要仔細設計和實施。

## 時間規劃與里程碑
*   Kindle Private Cloud AI Services已於去年11月發布。
*   持續開發和改進服務，並分享經驗和知識。

## 未解決的技術挑戰
*   如何在傳統數據中心中有效管理高密度GPU環境的電力和散熱。
*   如何在確保安全和合規性的同時，實現AI應用程式的靈活性和可擴展性。

## 後續行動計劃
*   繼續開發和改進Kindle Private Cloud AI Services。
*   分享實踐經驗和知識，幫助客戶構建主權AI。
*   與客戶和合作夥伴合作，推動AI創新。
