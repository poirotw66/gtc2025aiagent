# Isaac PerceptorとAutowareを組み合わせたNova Carterの自動運転 [S73870]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Isaac%20Perceptor%E3%81%A8Autoware%E3%82%92%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%81%9FNova%20Carter%E3%81%AE%E8%87%AA%E5%8B%95%E9%81%8B%E8%BB%A2%20%5BS73870%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1733321064657001yMQJ)
# Isaac Perceptor與Autoware結合的Nova Carter自動駕駛 [S73870]

## Key Takeaways
本次會議介紹了Tier4公司如何將NVIDIA Isaac Perceptor與Autoware自動駕駛軟體整合到NVIDIA Nova Carter自立移動機器人平台上，並展示了在實際場景中的應用。
### 重點摘要：
*   Tier4公司介紹及其在自動駕駛領域的貢獻，包括開源自動駕駛軟體Autoware。
*   NVIDIA Isaac Perceptor的介紹，特別是其在感知方面的能力，以及如何應用於自立移動機器人。
*   NVIDIA Nova Carter自立移動機器人平台的介紹，包括其硬體配置和軟體支援。
*   Autoware與Nova Carter的整合，展示了在室內環境中，Nova Carter如何使用Autoware進行自主導航和避障。
### Topic: 自動駕駛、機器人、感知、Autoware、Isaac Perceptor、Nova Carter

## 會議主題
會議主要探討了如何將NVIDIA Isaac Perceptor的感知能力與Autoware自動駕駛軟體整合到NVIDIA Nova Carter自立移動機器人平台上，實現自主導航和避障。

## 主要技術點
*   **Autoware架構：** 基於Linux和ROS2的開源自動駕駛軟體，提供完整的自動駕駛功能，包括感知、定位、規劃和控制。
*   **NVIDIA Isaac Perceptor：** 基於CUDA加速的ROS封裝，提供各種感知功能，包括深度學習推理、三維重建和視覺SLAM。
*   **NVIDIA Nova Carter：** 自立移動機器人平台，配備多種感測器，包括立體相機、魚眼相機和雷射雷達，並支援Isaac Perceptor。
*   **立體視覺：** 使用立體相機進行視差估計和三維重建，用於動態障礙物檢測和地圖構建。
*   **佔用柵格地圖：** 使用立體相機資訊建立佔用柵格地圖，用於導航和避障。
*   **車輛模型：** 定義車輛的控制輸入和幾何資訊，以便Autoware能夠控制Nova Carter。
*   **感測器模型：** 定義感測器的安裝位置、測量範圍和視野角，以便Autoware能夠使用感測器資訊。

## 決策與共識
*   使用NVIDIA Isaac Perceptor進行感知，以提高性能和效率。
*   使用Autoware作為自動駕駛軟體，以利用其成熟的功能和開源生態系統。
*   使用NVIDIA Nova Carter作為自立移動機器人平台，以簡化開發和部署。
*   將立體視覺作為主要的感知方式，以減少對雷射雷達的依賴。

## 時間規劃與里程碑
*   一個月的時間完成了Autoware與Nova Carter的整合。
*   成功在室內環境中演示了Nova Carter的自主導航和避障。
*   計畫未來改進立體匹配的深度學習模型，並使用更多的立體相機。
*   計畫將視覺里程計整合到Autoware中，並在室外環境中進行實驗。

## 未解決的技術挑戰
*   立體匹配的深度學習模型需要改進，以減少對地面附近障礙物的誤檢測。
*   視覺里程計尚未整合到Autoware中。
*   需要在室外環境中進行實驗，以驗證系統的魯棒性。

## 後續行動計劃
*   改進立體匹配的深度學習模型。
*   將視覺里程計整合到Autoware中。
*   使用四個立體相機建立佔用柵格地圖。
*   完善文件和範例，以便其他開發者可以輕鬆地將Autoware整合到Nova Carter中。
*   在Isaac Sim中建立模擬環境，並在室外環境中進行實驗。
