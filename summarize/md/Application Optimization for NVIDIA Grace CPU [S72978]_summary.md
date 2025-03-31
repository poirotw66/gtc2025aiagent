# Application Optimization for NVIDIA Grace CPU [S72978]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Application%20Optimization%20for%20NVIDIA%20Grace%20CPU%20%5BS72978%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1727952493311001tO28)
# NVIDIA Grace CPU 應用程式優化 [S72978]

## Key Takeaways
本會議主要介紹如何讓應用程式在 NVIDIA Grace CPU 上運行並進行優化。重點在於利用現有成熟的 ARM 生態系統，透過正確的編譯器、編譯器選項和優化函式庫，達到最佳效能。

### 重點摘要：
*   Grace CPU 簡介：基於 ARM Neoverse V2 核心，具有高效能和高功耗效率。
*   應用程式部署流程：強調 ARM 生態系統的成熟度，期望應用程式能直接運行，並提供優化建議。
*   優化策略：強調迭代式優化，先確保正確性，再追求效能，並以數據驅動的方式進行。

### Topic:
*   CPU 架構
*   效能優化
*   開發工具

## 會議主題
會議主要探討了如何針對 NVIDIA Grace CPU 架構優化應用程式，包括編譯器選擇、編譯選項設定、函式庫使用以及效能分析工具的運用。

## 主要技術點
*   **編譯器選擇：** 建議使用支援 Neoverse V2 的最新版本編譯器，例如 GCC、Clang 或 NVIDIA 自行構建的 Clang。
*   **編譯選項：** 推薦使用 `-O3`、`-mcpu=native` 和 `-ffp-contract=fast` 等選項，以針對 Grace CPU 進行優化。
*   **函式庫：** 建議使用 NVPL（NVIDIA Math Libraries）或 ARMPL 等針對 ARM 架構優化的函式庫，以提升線性代數運算效能。
*   **效能分析工具：** 介紹了 Perf、NVIDIA Nsight Systems 等工具，用於分析應用程式的效能瓶頸。
*   **硬體監控單元 (PMU)：** 介紹了 Core Events、Uncore Events 和 SPE (Statistical Profiling Extension) 等 PMU，用於監控 CPU 的硬體行為。
*   **SIMD 優化：** 討論了使用 SIMD 指令（例如 Neon 或 SV2）進行向量化優化的方法，包括編譯器自動向量化、OpenMP 指令和 Intrinsics。
*   **記憶體模型：** 簡要介紹了 ARM 的弱排序記憶體模型，以及如何使用 Atomic 操作確保多執行緒程式的正確性。

## 決策與共識
*   使用最新版本的編譯器和優化函式庫。
*   以數據驅動的方式進行效能分析和優化。
*   優先考慮程式碼的正確性，再追求效能。

## 時間規劃與里程碑
*   持續優化 NVPL 和 ARMPL 等函式庫，以提升在 Grace CPU 上的效能。
*   完善 NVIDIA Nsight Systems 等效能分析工具，提供更全面的 Grace CPU 支援。

## 未解決的技術挑戰
*   SPE (Statistical Profiling Extension) 工具的支援度有限，需要進一步完善。
*   ARM 的弱排序記憶體模型可能導致多執行緒程式出現問題，需要謹慎處理。

## 後續行動計劃
*   使用 NVIDIA Nsight Systems 進行效能分析，找出應用程式的瓶頸。
*   嘗試不同的編譯器選項和函式庫，以找到最佳的效能配置。
*   針對效能瓶頸進行程式碼優化，例如使用 SIMD 指令或調整記憶體存取模式。
*   驗證優化後的程式碼的正確性，確保沒有引入新的錯誤。
