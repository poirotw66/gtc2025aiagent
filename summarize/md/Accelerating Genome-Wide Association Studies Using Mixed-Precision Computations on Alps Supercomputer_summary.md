# Accelerating Genome-Wide Association Studies Using Mixed-Precision Computations on Alps Supercomputer
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Accelerating%20Genome-Wide%20Association%20Studies%20Using%20Mixed-Precision%20Computations%20on%20Alps%20Supercomputer&tab.catalogallsessionstab=16566177511100015Kus#/session/1726202031896001Pr8c)
# 使用混合精度計算在 Alps 超級電腦上加速全基因組關聯研究

## Key Takeaways
本會議介紹了使用混合精度計算在 Alps 超級電腦上加速全基因組關聯研究 (GWAS) 的方法。重點在於利用低精度 tensor core 加速計算，並結合 kernel ridge regression 方法，以提高 GWAS 的效率和準確性。
### 重點摘要：
*   利用混合精度計算加速 GWAS，特別是使用 FP8 和 Integer 8 tensor core。
*   採用 kernel ridge regression 方法，相較於 ridge regression，能更有效地建模複雜的表型關係。
*   在多個超級電腦上進行了實驗，包括 Alps、Frontier、Leonardo 和 Summit，展示了軟體的移植性和性能。
*   實現了 1.8 exaops 的性能，相較於傳統 CPU 方法有顯著的加速。
### Topic: Genomics, High Performance Computing, Mixed-Precision Computing

## 會議主題
會議主要探討了如何利用混合精度計算和 kernel ridge regression 方法，在 GPU 上加速全基因組關聯研究 (GWAS)。重點在於利用低精度 tensor core (FP8 和 Integer 8) 加速計算，並結合資料稀疏性優化，以提高 GWAS 的效率和準確性。

## 主要技術點
*   **混合精度計算：** 根據資料的特性，動態調整計算精度，以在保證準確性的前提下，最大化計算效率。使用了 FP8、FP16、FP32 和 FP64 等多種精度。
*   **Kernel Ridge Regression：** 使用 kernel 方法建模 SNP 之間的複雜非線性關係，相較於傳統的 ridge regression，能更有效地捕捉表型與基因型之間的關聯。
*   **Tensor Core 加速：** 利用 NVIDIA GPU 上的 tensor core 加速矩陣乘法等計算密集型操作，特別是使用 Integer 8 tensor core 加速基因型距離計算。
*   **資料稀疏性優化：** 利用 kernel 矩陣的資料稀疏性，減少計算量和記憶體佔用，提高計算效率。
*   **Tile-based Linear Algebra：** 使用基於 tile 的線性代數方法，將大型矩陣分解成小塊，以便在多個 GPU 上並行計算。
*   **Adaptive Precision Algorithm：** 根據 tile 的特性，動態選擇計算精度，以在保證準確性的前提下，最大化計算效率。
*   **Cholesky 分解：** 使用 Cholesky 分解求解線性方程組，這是 GWAS 計算中的一個關鍵步驟。

## 決策與共識
*   採用混合精度計算和 kernel ridge regression 方法，以提高 GWAS 的效率和準確性。
*   利用 NVIDIA GPU 上的 tensor core 加速計算，特別是使用 Integer 8 tensor core 加速基因型距離計算。
*   利用資料稀疏性優化，減少計算量和記憶體佔用，提高計算效率。
*   在多個超級電腦上進行實驗，以驗證軟體的移植性和性能。

## 時間規劃與里程碑
*   開發能夠執行 multivariate GWAS 的軟體工具，以檢測使用 kernel ridge regression 的複雜上位性。
*   將距離計算轉換為 Gram 矩陣的 tensor core。
*   使用混合精度加速計算，並利用新的 FP8。
*   證明 kernel ridge regression 優於 ridge regression 的準確性。
*   在 Alps 上以 1300 萬患者實現 1.8 exaops。

## 未解決的技術挑戰
*   如何更好地利用 3D 基因組的空間局部性，例如原子接觸圖。
*   如何改進對複雜威脅的綜合效應的檢測。
*   如何利用低秩矩陣近似來利用資料稀疏性。

## 後續行動計劃
*   利用 3D 基因組的空間局部性，例如原子接觸圖，以提高 GWAS 的準確性。
*   改進對複雜威脅的綜合效應的檢測。
*   利用低秩矩陣近似來利用資料稀疏性，以減少計算量和記憶體佔用。
*   將該方法應用於其他基因組研究，例如小麥基因組研究。
