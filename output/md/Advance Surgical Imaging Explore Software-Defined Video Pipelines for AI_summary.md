# Advance Surgical Imaging Explore Software-Defined Video Pipelines for AI
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Advance%20Surgical%20Imaging%20Explore%20Software-Defined%20Video%20Pipelines%20for%20AI&search=Advance+Surgical+Imaging+Explore+Software-Defined+Video+Pipelines+for+AI&tab.catalogallsessionstab=16566177511100015Kus#/session/1737533643034001cttG)
# Advance Surgical Imaging Explore Software-Defined Video Pipelines for AI

## Key Takeaways
本次會議主要討論了軟體定義視訊管線在手術應用中的潛力，特別是利用 NVIDIA IGX 和 Holoscan SDK 來實現即時影像處理和 AI 加速。會議涵蓋了傳統硬體管線的局限性，以及軟體定義方法如何提供更大的靈活性、可擴展性和 AI 整合能力。

### 重點摘要：
*   傳統硬體視訊管線的局限性，包括固定功能、擴展性和靈活性不足，以及整合 AI 的困難。
*   軟體定義視訊管線的優勢，包括靈活性、可擴展性、AI 整合能力，以及簡化新設備開發的潛力。
*   NVIDIA IGX 和 Holoscan SDK 在構建軟體定義視訊管線中的作用，包括提供強大的硬體平台、高效的資料傳輸能力和易於使用的軟體工具。
*   Kallstolz 公司在手術影像領域的經驗和挑戰，以及他們如何利用軟體定義視訊管線來改進手術影像品質和提供 AI 輔助功能。

### Topic:
*   軟體定義視訊管線
*   手術影像
*   AI 加速
*   NVIDIA IGX
*   Holoscan SDK

## 會議主題
會議主要探討了如何利用軟體定義視訊管線來改進手術影像品質，並將 AI 整合到手術工作流程中。會議重點關注了 NVIDIA IGX 和 Holoscan SDK 在實現這些目標中的作用。

## 主要技術點
*   **傳統硬體視訊管線 (FPGA)**：
    *   優點：高效能、低延遲。
    *   缺點：固定功能、擴展性差、靈活性低、AI 整合困難、開發週期長、成本高。
*   **軟體定義視訊管線 (GPU)**：
    *   優點：靈活性高、可擴展性強、易於整合 AI、開發週期短、成本較低。
    *   缺點：效能可能不如 FPGA、可能存在延遲和抖動。
*   **NVIDIA IGX**：
    *   提供強大的硬體平台，包括 GPU、安全 MCU 和 ConnectX-7 網路卡。
    *   ConnectX-7 提供高頻寬資料傳輸，支援直接將資料從網路傳輸到 GPU 記憶體。
    *   安全 MCU 監控系統效能，確保系統安全可靠。
*   **Holoscan SDK**：
    *   提供易於使用的軟體工具，簡化軟體定義視訊管線的開發。
    *   支援自定義運算元，允許開發者針對特定應用優化影像處理流程。
    *   整合 CUDA 和 NPP，充分利用 GPU 的效能。
*   **影像處理流程**：
    *   從感測器獲取原始資料。
    *   進行預處理，包括重新計時、黑電平校正、非均勻性校正等。
    *   進行 demosaicking，將原始資料轉換為 RGB 影像。
    *   進行色彩校正和白平衡。
    *   應用秘密濾鏡，增強影像品質。
    *   整合 AI 模型，進行異常檢測、匿名化等。
    *   使用 HoloVis 渲染影像。

## 決策與共識
*   軟體定義視訊管線是手術影像領域的未來發展方向。
*   NVIDIA IGX 和 Holoscan SDK 是構建軟體定義視訊管線的理想平台。
*   需要開發自定義運算元，以滿足手術影像的特定需求。
*   需要優化軟體定義視訊管線的效能，以實現即時影像處理。

## 時間規劃與里程碑
*   目前正在使用 Holoscan SDK 開發自定義運算元。
*   目標是在未來幾年內將軟體定義視訊管線整合到 Kallstolz 的產品中。
*   持續優化軟體定義視訊管線的效能，以實現更低的延遲和更高的影像品質。

## 未解決的技術挑戰
*   如何實現與 FPGA 相當的效能和低延遲。
*   如何處理不同感測器和晶片的資料格式差異。
*   如何確保軟體定義視訊管線的穩定性和可靠性。

## 後續行動計劃
*   繼續開發和優化自定義運算元。
*   評估不同的硬體平台，包括 NVIDIA IGX 和其他 GPU。
*   進行廣泛的測試，以驗證軟體定義視訊管線的效能和可靠性。
*   與手術醫生合作，收集反饋並改進系統。
