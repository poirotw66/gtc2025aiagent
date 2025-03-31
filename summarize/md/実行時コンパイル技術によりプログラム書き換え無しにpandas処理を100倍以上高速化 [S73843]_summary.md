# 実行時コンパイル技術によりプログラム書き換え無しにpandas処理を100倍以上高速化 [S73843]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E5%AE%9F%E8%A1%8C%E6%99%82%E3%82%B3%E3%83%B3%E3%83%8F%E3%82%9A%E3%82%A4%E3%83%AB%E6%8A%80%E8%A1%93%E3%81%AB%E3%82%88%E3%82%8A%E3%83%95%E3%82%9A%E3%83%AD%E3%82%AF%E3%82%99%E3%83%A9%E3%83%A0%E6%9B%B8%E3%81%8D%E6%8F%9B%E3%81%88%E7%84%A1%E3%81%97%E3%81%ABpandas%E5%87%A6%E7%90%86%E3%82%92100%E5%80%8D%E4%BB%A5%E4%B8%8A%E9%AB%98%E9%80%9F%E5%8C%96%20%5BS73843%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1733124364226001p5E3)
# 透過執行時編譯技術，無需修改程式碼即可將 Pandas 處理速度提高 100 倍以上 [S73843]

## Key Takeaways
本次演講介紹了 NEC 開發的 FireDux 函式庫，該函式庫透過執行時編譯技術，在不改變 Pandas API 的情況下，大幅提升 Pandas 程式的執行速度。FireDux 利用 NVIDIA 的 QDF 函式庫，在 GPU 上執行 Pandas 運算，並透過多種最佳化策略，進一步提升效能。
### 重點摘要：
*   FireDux 是一個高速資料框架函式庫，旨在加速 Pandas 程式的執行。
*   FireDux 透過執行時編譯器和 GPU 加速，實現顯著的效能提升。
*   FireDux 與 Pandas API 相容，使用者只需修改 import 語句即可使用。
*   FireDux 採用多種最佳化策略，包括投影下推、模式最佳化等。
*   FireDux 的 GPU 後端基於 NVIDIA 的 QDF 函式庫。
### Topic: 資料科學、GPU 加速、執行時編譯

## 會議主題
會議主要介紹了 FireDux 函式庫的架構、最佳化策略和效能評估，展示了如何利用 FireDux 在 GPU 上高速執行 Pandas 程式。

## 主要技術點
*   **執行時編譯 (JIT Compilation):** FireDux 使用執行時編譯器，在程式執行時對 Pandas 程式碼進行最佳化，並編譯成高效能的 GPU 程式碼。
*   **資料框架中間語言 (IR):** FireDux 使用一種專為資料框架操作設計的中間語言，方便進行各種最佳化。
*   **投影下推 (Projection Pushdown):** 一種最佳化策略，將欄位選擇操作提前到資料讀取階段，減少不必要的資料處理。
*   **模式最佳化 (Pattern Optimization):** 一種最佳化策略，將常見的 Pandas 程式碼模式替換為更高效的實現方式。
*   **GPU 後端:** FireDux 利用 NVIDIA 的 QDF 函式庫，在 GPU 上執行資料框架操作，實現高度並行化和加速。
*   **Define-by-Run 方式:** FireDux 使用 Define-by-Run 方式生成中間語言，即在程式執行過程中逐步構建中間語言表示。
*   **Fallback 機制:** FireDux 具有 Fallback 機制，當遇到不支援的 Pandas 功能時，會自動切換回 Pandas 執行，保證程式的相容性。

## 決策與共識
*   採用執行時編譯和 GPU 加速，以提升 Pandas 程式的執行速度。
*   使用資料框架中間語言，方便進行各種最佳化。
*   利用 NVIDIA 的 QDF 函式庫，在 GPU 上執行資料框架操作。
*   提供 Fallback 機制，保證程式的相容性。

## 時間規劃與里程碑
*   2025 年中發布 FireDux。
*   CPU 版本已在 PyPI 上發布。

## 未解決的技術挑戰
*   QDF 函式庫與 Pandas 的行為存在細微差異，需要進行調整以保證相容性。
*   需要不斷擴充 FireDux 的支援功能，減少 Fallback 的使用。

## 後續行動計劃
*   繼續開發和最佳化 FireDux 函式庫。
*   擴充 FireDux 的支援功能，減少 Fallback 的使用。
*   與 NVIDIA 合作，提升 QDF 函式庫的效能和相容性。
*   發布 FireDux，供使用者使用和回饋。
