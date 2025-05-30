# 下一代生成式推薦模型訓推引擎的建設和落地實踐
[會議影片連結](https://www.nvidia.com/gtc/session-catalog/?search=%E4%B8%8B%E4%B8%80%E4%BB%A3%E7%94%9F%E6%88%90%E5%BC%8F%E6%8E%A8%E8%8D%90%E6%A8%A1%E5%9E%8B%E8%AE%AD%E6%8E%A8%E5%BC%95%E6%93%8E%E7%9A%84%E5%BB%BA%E8%AE%BE%E5%92%8C%E8%90%BD%E5%9C%B0%E5%AE%9E%E8%B7%B5&tab.catalogallsessionstab=16566177511100015Kus#/session/1734091150868001dcjp)
下一代生成式推薦模型訓推引擎的建設和落地實踐

## Key Takeaways
本次會議介紹了美團下一代生成式推薦模型，迅推引擎（MTGR）的建設和落地實踐。重點在於解決生成式推薦模型訓練和推理所面臨的挑戰，包括訓練成本高、推理延遲嚴格等問題。
### 重點摘要：
*   **背景介紹：** 說明了為何要採用生成式推薦，以及傳統推薦系統的瓶頸。
*   **模型介紹：** 闡述了生成式推薦模型的設計思路，參考 Meta 的 GIA 模型，並根據美團的實際情況進行調整。
*   **MTGR 介紹：** 詳細介紹了美團為生成式推薦模型所建設的訓練推薦引擎 MTGR，包括其架構、核心組件和優化策略。
*   **總結與展望：** 總結了 MTGR 的優勢，並展望了未來的工作方向，包括實時學習、性能優化、模型規模擴展等。
### Topic:
*   生成式推薦模型
*   模型訓練引擎
*   模型推理引擎
*   性能優化

## 會議主題
會議主要探討了美團如何基於生成式思想，構建下一代推薦模型，並通過自研的 MTGR 引擎，解決模型訓練和推理所面臨的性能挑戰，最終實現生成式推薦模型在外賣場景下的落地應用。

## 主要技術點
*   **生成式推薦模型：** 採用序列化的方式組織特徵，利用自迴歸的方式預測下一個點擊 item 的概率分佈。
*   **Listwise 建模：** 採用 Listwise 的方式替代 Pondwise 的方式做建模，提升訓練和推理效率。
*   **UserModel 設計：** 採用中 UserModel 的設計，並儘量復用 KPcatch，減少重複計算，提升整理吞吐。
*   **MTGR Training：** 基於 TouchRack 構建，支持低成本、高效率的大規模分佈式訓練，包括動態 Hash Table、梯度累積、通信優化等功能。
*   **混合並行策略：** 採用 Spas 部分模型並行，加 Dense 部分數據並行的混合並行策略。
*   **自動合表：** 設計實現一套吸收源與 API，用戶僅需定義特徵的關鍵屬性，即可自動生成模型的 SPAS 部分，並且對多個吸收表進行自動合併。
*   **Kernel 優化：** 集成 NVIDIA 提供的深度優化的 Catalyst-based HSTU kernel，大幅提升了 Attention 的計算效率。
*   **變長序列負載均衡：** 引入動態 Batch Size，每張卡的 Batch Size 根據實際的數據序列長度動態調整，從而保證計算量基本相同。
*   **MTGR Inference：** 基於 Tensor RT 和 TrickInference Server，支持低延遲、高吞吐的大規模線上推理部署，包括特徵 H2D 優化、CUDA Graph 優化、HashiTable 優化等。
*   **User Cache：** 按照用戶力度存儲序列的計算結果，新請求到來時，首先通過 UserID 在 Cache Server 上查詢，減少重複計算。

## 決策與共識
*   採用生成式推薦模型作為下一代推薦模型，以提升模型效果和泛化能力。
*   自研 MTGR 引擎，以解決生成式推薦模型訓練和推理所面臨的性能挑戰。
*   採用混合並行策略、自動合表、Kernel 優化、變長序列負載均衡等技術，提升訓練效率。
*   採用特徵 H2D 優化、CUDA Graph 優化、HashiTable 優化、User Cache 等技術，提升推理效率。

## 時間規劃與里程碑
*   已完成 MTGR 引擎的建設，並在美團外賣場景下落地應用。
*   未來將持續優化 MTGR 引擎，並探索更多模型優化和加速技術。
*   計劃將 MTGR 引擎應用於更多業務場景，支持更大規模的生成式推薦模型。

## 未解決的技術挑戰
*   GR 模型尚未支持實時學習，需要將 GR 模型和實時學習結合起來。
*   Embiting 壓縮、低精度訓練等優化手段還有較大的性能提升空間。
*   需要支持 Dense 模型的並行訓練，以支持更大規模的 GR 模型。

## 後續行動計劃
*   將 GR 模型和實時學習結合起來，提升模型的實時性和準確性。
*   探索 Embiting 壓縮、低精度訓練等優化手段，進一步提升性能。
*   支持 Dense 模型的並行訓練，以支持更大規模的 GR 模型。
*   嘗試 AOT Compile，通過編譯優化手段，進一步提升 PiTouch 模型性能。
