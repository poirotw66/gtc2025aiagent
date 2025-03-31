# Advance Surgical Imaging Explore Software-Defined Video Pipelines for AI
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Advance%20Surgical%20Imaging%20Explore%20Software-Defined%20Video%20Pipelines%20for%20AI&search=Advance+Surgical+Imaging+Explore+Software-Defined+Video+Pipelines+for+AI&tab.catalogallsessionstab=16566177511100015Kus#/session/1737533643034001cttG)
# 先進手術影像探索用於AI的軟體定義視訊管線

## Key Takeaways
本次會議主要討論了Kallstolz公司在手術應用中，從傳統硬體定義視訊管線轉向軟體定義視訊管線的策略、挑戰與優勢。重點在於利用NVIDIA IGX Orin和Holoscan SDK，實現即時AI加速功能，提升手術影像品質與效率，最終改善患者護理。
### 重點摘要：
*   Kallstolz公司是一家醫療設備公司，專注於為外科醫生提供創新技術。
*   傳統硬體定義管線的局限性：固定功能、擴展性差、AI整合困難、硬體更新週期慢。
*   軟體定義管線的優勢：靈活性高、易於整合AI、可快速適應新硬體和演算法。
*   利用NVIDIA IGX Orin和Holoscan SDK，克服即時處理和AI整合的挑戰。
*   客製化CUDA核心和NPP（NVIDIA Performance Primitives）對於實現高效能至關重要。
### Topic: 醫療影像、AI加速、軟體定義管線

## 會議主題
會議主要探討了如何利用軟體定義視訊管線，特別是NVIDIA IGX Orin和Holoscan SDK，來改善手術影像處理。重點包括從原始感測器數據到最終顯示影像的整個流程，以及如何在這個流程中整合AI功能，以提升手術效果。

## 主要技術點
*   **原始數據處理：** 從相機晶片獲取原始讀數，進行重新定時、黑階校正、非均勻性校正等預處理。
*   **圖像重建：** 使用demosaicking演算法將原始晶片數據轉換為RGB圖像。
*   **色彩校正：** 調整色彩平衡，突出顯示對外科醫生重要的組織細節（如紅色、紫色、藍色）。
*   **曝光控制：** 實時調整曝光，以應對手術過程中光線變化的挑戰。
*   **AI整合：** 在管線的不同階段整合AI模型，例如用於患者數據匿名化、異常檢測等。
*   **NVIDIA IGX Orin：** 利用其強大的計算能力、安全MCU和高速網路連接，實現即時處理和安全監控。
*   **Holoscan SDK：** 使用其提供的工具和框架，簡化軟體定義管線的開發和部署。
*   **CUDA核心和NPP：** 客製化CUDA核心和使用NPP，以優化特定圖像處理任務的效能。

## 決策與共識
*   軟體定義視訊管線是未來手術影像處理的發展方向。
*   NVIDIA IGX Orin和Holoscan SDK是實現軟體定義管線的理想平台。
*   需要客製化開發，以滿足手術影像處理的特定需求。
*   在效能、延遲、靈活性和成本之間取得平衡。

## 時間規劃與里程碑
*   目前已成功建立基於Holoscan的簡化管線，延遲約為30毫秒。
*   持續優化管線，以達到與現有FPGA系統相當的效能水平（60毫秒）。
*   整合更多AI功能，並將其部署到實際手術環境中。

## 未解決的技術挑戰
*   如何在軟體定義管線中實現與FPGA相當的低延遲和穩定性。
*   如何有效地管理和優化GPU資源，以應對複雜的圖像處理和AI任務。
*   如何確保系統的安全性，並符合醫療設備的相關標準。

## 後續行動計劃
*   繼續開發和優化客製化CUDA核心和NPP。
*   探索更多AI整合的可能性，例如用於手術導航、增強現實等。
*   與外科醫生合作，收集反饋，並不斷改進系統。
*   進行全面的驗證和測試，以確保系統的可靠性和安全性。
