# Isaac PerceptorとAutowareを組み合わせたNova Carterの自動運転 [S73870]
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=Isaac%20Perceptor%E3%81%A8Autoware%E3%82%92%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%81%9FNova%20Carter%E3%81%AE%E8%87%AA%E5%8B%95%E9%81%8B%E8%BB%A2%20%5BS73870%5D&tab.catalogallsessionstab=16566177511100015Kus#/session/1733321064657001yMQJ)
# Isaac Perceptor與Autoware結合的Nova Carter自動駕駛 [S73870]

## Key Takeaways
本次會議介紹了Tier4公司如何將NVIDIA Isaac Perceptor與自動駕駛軟體Autoware整合到NVIDIA Nova Carter自立移動機器人平台上，並展示了在品川辦公室咖啡區的實際運行效果。重點在於Autoware的斜線導航特性，以及利用立體相機資訊建立佔用網格地圖，實現動態障礙物避讓。
### 重點摘要：
*   展示了NVIDIA Nova Carter在Autoware控制下於室內環境中自主移動的成果。
*   介紹了使用NVIDIA Isaac Perceptor進行感知，並利用立體相機資訊建立佔用網格地圖的方法。
*   分享了將Autoware整合到Nova Carter的過程，包括車輛模型適配和感測器模型適配。
### Topic:
*   自動駕駛
*   機器人
*   感知

## 會議主題
會議主要探討了如何將NVIDIA Isaac Perceptor感知能力與Autoware自動駕駛軟體整合到NVIDIA Nova Carter平台上，實現自主導航和障礙物避讓。

## 主要技術點
*   **Autoware斜線導航：** Autoware與其他導航軟體不同，具備沿斜線移動的特性，可根據向量地圖進行導航。
*   **立體相機佔用網格地圖：** 使用立體相機資訊建立佔用網格地圖，用於識別動態障礙物。
*   **車輛模型適配：** 將Autoware的控制指令轉換為Nova Carter的作動二軸控制指令。
*   **感測器模型適配：** 將Nova Carter的感測器資訊（如雷射雷達、IMU、相機）轉換為Autoware可用的格式。
*   **Isaac ROS Visual SLAM：** 使用Isaac ROS Visual SLAM進行視覺定位和地圖建立，但存在對地面障礙物誤判的問題。
*   **Isaac Sim模擬：** 使用Isaac Sim進行Autoware的模擬測試，驗證系統的可靠性。

## 決策與共識
*   採用Autoware作為自動駕駛軟體，利用其斜線導航特性。
*   使用NVIDIA Isaac Perceptor進行感知，並利用立體相機資訊建立佔用網格地圖。
*   將開發的Autoware整合套件以Apache 2.0授權在GitHub上公開。

## 時間規劃與里程碑
*   開發週期為一個月。
*   成功將Autoware整合到Nova Carter平台。
*   在品川辦公室咖啡區進行了實際運行測試。

## 未解決的技術挑戰
*   Isaac ROS Visual SLAM對地面障礙物存在誤判，需要改進立體匹配的深度學習模型。
*   視覺里程計尚未完全整合到Autoware中，目前仍使用雷射雷達定位。

## 後續行動計劃
*   改進Isaac Perceptor的立體匹配推論，提高對地面障礙物的識別精度。
*   使用四個立體相機建立佔用網格地圖，擴大感知範圍。
*   完善Autoware整合套件的文檔，使其更易於使用。
*   改進Autoware的設計，使其更好地支援視覺感測器。
*   建立更真實的Isaac Sim模擬環境，並進行戶外實驗。
