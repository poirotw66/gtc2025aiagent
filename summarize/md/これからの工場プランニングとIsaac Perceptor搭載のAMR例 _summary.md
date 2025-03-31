# これからの工場プランニングとIsaac Perceptor搭載のAMR例
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E3%81%93%E3%82%8C%E3%81%8B%E3%82%89%E3%81%AE%E5%B7%A5%E5%A0%B4%E3%83%95%E3%82%9A%E3%83%A9%E3%83%B3%E3%83%8B%E3%83%B3%E3%82%AF%E3%82%99%E3%81%A8Isaac%20Perceptor%E6%90%AD%E8%BC%89%E3%81%AEAMR%E4%BE%8B%20&tab.catalogallsessionstab=16566177511100015Kus#/session/1733391520503001nAJy)
# 未來工廠規劃與搭載 Isaac Perceptor 的 AMR 範例

## Key Takeaways
武藏AI株式会社介紹了其在生產現場創造價值的數位雙生技術，以及未來工廠規劃和搭載 iZEC Perceptor 的 AMR 範例。重點在於利用 NVIDIA Isaac Perceptor 提升 AMR 的性能，並將數位雙生技術應用於工廠模擬和優化。
### 重點摘要：
*   武藏AI株式会社的業務概要、活動案例以及未來願景。
*   介紹了 AI 外觀檢查裝置和 AMR 的應用案例，以及導入效果。
*   闡述了利用數位雙生技術和工廠能源管理系統實現智慧工廠的目標。
*   深入探討了 NVIDIA Isaac Perceptor 在 AMR 中的應用，包括 DNN 立體深度、姿態估計、圖像分割和 KOOV SLAM。
*   展示了利用數位雙生進行 AMR 模擬，包括 SLAM 功能、物理特性和機器人手臂的模擬。
### Topic: AMR、數位雙生、智慧工廠

## 會議主題
會議主要探討了如何利用 NVIDIA Isaac Perceptor 提升 AMR 的性能，並將數位雙生技術應用於工廠模擬和優化，以實現更高效、更靈活的智慧工廠。

## 主要技術點
*   **NVIDIA Isaac Perceptor：** 一個基於 ROS 的整合感測管道，利用 GPU 加速，用於 AMR 的自我定位、環境映射和導航。
*   **DNN 立體深度 (DNN Stereo Depth)：** 利用深度學習進行高精度距離估計，優於傳統深度相機，提升 AMR 在搬運對象識別和視覺 SLAM 方面的魯棒性。
*   **姿態估計 (Pose Estimation)：** 利用深度學習估計人物和物體的 3D 姿態，使 AMR 能夠判斷搬運對象的位置和角度，實現更靈活的搬運。
*   **圖像分割 (Image Segmentation)：** 對圖像中的物體進行分割和識別，使 AMR 能夠區分人和物體，並根據情況採取不同的行動。
*   **KOOV SLAM：** 一個基於立體相機的視覺里程計模組，用於機器人的自我定位，並通過迴路閉合功能解決傳統里程計的漂移問題。
*   **NV Blocks：** 用於構建周圍環境的 3D 模型，支持導航和 SLAM 功能，並可應用於數位雙生。
*   **數位雙生 (Digital Twin)：** 通過模擬真實工廠環境，進行 AMR 的虛擬測試和優化，包括 SLAM 功能、物理特性和機器人手臂的模擬。

## 決策與共識
*   利用 NVIDIA Isaac Perceptor 提升 AMR 的性能，實現更精確的自我定位、環境感知和導航。
*   將數位雙生技術應用於工廠模擬和優化，降低開發成本，提高效率。
*   通過整合 AMR、FA 技術、IoT 和 AI 檢查技術，實現智慧工廠。

## 時間規劃與里程碑
*   利用 Nova Allin Developer Kit 進行 Isaac Perceptor 功能的開發和 AMR 整合。
*   將 Isaac Perceptor 功能部署到 AMR 上，並進行實際測試和驗證。
*   繼續開發數位雙生技術，並將其應用於工廠模擬和優化。

## 未解決的技術挑戰
*   如何進一步提高 Isaac Perceptor 的精度和魯棒性。
*   如何將數位雙生技術更有效地應用於工廠的各個方面。
*   如何降低智慧工廠的建設成本。

## 後續行動計劃
*   繼續與 NVIDIA 合作，利用其最新的技術和解決方案。
*   加強與客戶的合作，了解其需求，並提供定制化的解決方案。
*   不斷創新，開發新的技術和產品，以滿足市場的需求。
