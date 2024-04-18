# 基于共享单车骑行数据的上海市通勤模式分析

## 数据

## 要点
1. [GeoHash](https://zhuanlan.zhihu.com/p/35940647) 
   1. [在线工具](https://csxgame.top/#/) 
   2. [资料](https://www.goitman.cn/2021/11/02/%E7%BB%8F%E7%BA%AC%E5%BA%A6%E7%9A%84Geohash%E7%AE%97%E6%B3%95%E4%B8%8E%E4%B8%A4%E7%82%B9%E8%B7%9D%E7%A6%BB%E7%AE%97%E6%B3%95/)
   3. [geoTree](https://arxiv.org/pdf/2008.02167.pdf)
2. [DBSCAN](https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/): Density-Based Spatial Clustering of Applications with Noise
   1. [使用 DBSCAN 聚类算法剔除异常矩形](https://kyle.ai/blog/7568.html)
3. [轨迹聚类](https://hanj.cs.illinois.edu/pdf/sigmod07_jglee.pdf)
   1. [轨迹聚类TraClus的学习笔记](https://zhuanlan.zhihu.com/p/644217934)
   2. [traclus-python](https://pypi.org/project/traclus-python/)
   3. [trajectory-cluster](https://github.com/MillerWu2014/trajectory-cluster?tab=readme-ov-file)
4. [空间相关性](https://image.hanspub.org/html/11-2580204_19443.htm)
   1. [莫兰指数](https://zh.wikipedia.org/wiki/%E8%8E%AB%E5%85%B0%E6%8C%87%E6%95%B0)：属性值与位置之间的关系，譬如某种疾病的发病率与地理位置之间的关系。
   2. [皮尔逊积矩相关系数](https://zh.wikipedia.org/wiki/%E7%9A%AE%E5%B0%94%E9%80%8A%E7%A7%AF%E7%9F%A9%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0)

## 关键词

## 参考文献
[1]李文翔,唐桂孔,刘博,等.基于摩拜骑行数据的上海市共享单车减排效益时空分析[J].环境科学学报,2021,41(11):4752-4759.DOI:10.13671/j.hjkxxb.2021.0213.
[2]王若萱,吴建平,奇格奇. 基于上海市数据的共享单车用户通勤模式研究（英文）[C]中国仿真学会.第三十三届中国仿真大会论文集.2021:16.DOI:10.26914/c.cnkihy.2021.025005.
[3]全雨霏. 南京市共享单车使用的时空特征及其骑行环境评估[D].东南大学,2024.DOI:10.27014/d.cnki.gdnau.2022.001097.
[4]常新. 基于共享单车轨迹数据的城市街道可骑行性研究[D].哈尔滨工业大学,2021.DOI:10.27061/d.cnki.ghgdu.2020.002483.
[5]Jie Bao, Tianfu He, Sijie Ruan , Yanhua Li, and Yu Zheng. 2017. Planning Bike Lanes based on Sharing-Bikes’ Trajectories[c]. In Proceedings of KDD’17, August 13–17, 2017, Halifax, NS, Canada., , 11 pages.
[6]刘泉宏,唐福星.基于K-means聚类算法与重心法的故障共享单车回收中心选址优化[J].运筹与管理,2023,32(07):85-91.
[7]谢光明. 基于改进时空图神经网络的共享单车流量预测[D].华东师范大学,2023.DOI:10.27149/d.cnki.ghdsu.2023.004430.
[8]刘冰,王舸洋,朱俊宇,等.基于共享单车大数据的骑行生活圈识别及其活动网络模式分析[J].城市规划学刊,2023(04):32-40.DOI:10.16361/j.upf.202304005.
[9]王俊,于爱荣.基于ConvLSTM的南京地区共享单车需求预测研究[J].软件工程,2024,27(02):55-59.DOI:10.19644/j.cnki.issn2096-1472.2024.002.011.
[10]谢国微. 天气及建成环境对共享单车出行需求的影响研究[D].南京林业大学,2024.DOI:10.27242/d.cnki.gnjlu.2022.000493.
[11]任丹. 基于TRACLUS算法的船舶轨迹分析系统的设计与实现[D].辽宁师范大学,2021.DOI:10.27212/d.cnki.glnsu.2020.001211.


[12]洪文兴,陈明韬,刘伊灵,等.基于GeoHash和HDBSCAN的共享单车停车拥挤区域识别[J].厦门大学学报(自然科学版),2022,61(06):1030-1037.
[13]王小霞,欧阳露,郑诗琪,等.GeoHash与KNN在共享单车停靠点优化选择中的应用[J].广东工业大学学报,2022,39(03):1-7.
[14]张海亮,张征.基于GeoHash索引的A~*算法优化[J].火力与指挥控制,2021,46(06):78-83.
[15]陈刚,王国新,明振军,等.基于DBSCAN聚类和LSTM网络的装甲车辆集群轨迹预测方法[J/OL].兵工学报:1-16[2024-04-17].http://kns.cnki.net/kcms/detail/11.2176.tj.20240201.1104.002.html.

## 参考文献链接
1. [基于摩拜骑行数据的上海市共享单车减排效益时空分析](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7NNnM-YGQFY7OR0Yl83BKx9EFlh2sdl5giU7icp05a8kf6t0xd3GfTZ3PSgqRqWIi0qbf8hp_wlVQMQaJD45fvBgd3vh3y8B4WGvAanVVI2S5Sc_malTmUDqREAIlsSmVbPtaOTCyzktw==&uniplatform=NZKPT&language=CHS)
2. [基于上海市数据的共享单车用户通勤模式研究（英文）](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7OU4OLiJXnH9KqW1K7aWatIgv0mqph8HG19CNWC_qUAK-cCryG4M3Jsjvcy-HAM_mbfE6NReo5aHsF0a3_Okw3E_XO1xyQgXp2Jalpo0t2hDlN-Qj_gM1H30tfNV5dkkH-tzNFlEeF9MQ==&uniplatform=NZKPT&language=CHS)
3. [南京市共享单车使用的时空特征及其骑行环境评估——以主城区为例](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7MnxMRCMNtuXvLrIKiqmBPwK29N1SYIS3RRCS8O1wgteu521IlsmjLuGmfs4bbo8gaC55CanReU-_F6tsTgltxpTSQeGRVmjE2QEHuDPIIT8FgP0WCnilpvRWG3_aimKgOpZzyfe9oVfw==&uniplatform=NZKPT&language=CHS)
4. [基于共享单车轨迹数据的城市街道可骑行性研究——以深圳市龙岗区为例](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7NjB2aUkyFI1WWKO4QTByJus8AqwrsWRwcsYCn17YIMbn7TQFd7DHMrt7Fp9-UcDmKwDZj2FOU2MwHFE9DRvadVQ50PsERgZqcNhe66yXo-1o6mNqwvfR3Dwgasx5PKKB8Cp7n6hrLZHg==&uniplatform=NZKPT&language=CHS)
5. [Planning Bike Lanes based on Sharing-Bikes’ Trajectories](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/main.pdf) [知乎](https://daily.zhihu.com/story/9626002)
6. [基于K-means聚类算法与重心法的故障共享单车回收中心选址优化](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7PsTSAp1z_g0kcY5dQHru-g24P3r_5C_YHJUixnAvVnLohcUIqCw8Gk2u16V2eh6QCUhM-Gb1pET7wbLpIsTByq3XmxlHwUCXyyZaqsZP4xjwUReZ2bJdkG&uniplatform=NZKPT&language=gb)
7. [基于改进时空图神经网络的共享单车流量预测](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7NOOW09A6ZQof-wKjxnzmwRlajsyKBCjBO3xD20_1lmqk5x-fz2o1tXPaPUdWT2cz3Sd0AdKfDVX9tDu2plMTHVCOeFogzbF4wOxrQ9X9z6UQ==&uniplatform=NZKPT&language=gb)
8. [基于共享单车大数据的骑行生活圈识别及其活动网络模式分析](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7MYvY6iMopn_YMvPbyF4NICs-UidzcjMZKRAVtyVMifLpVmpccBXep9NR_tQwWiguij0H3K3JP5n-wtBu4fduoxtNg_pR0dLJEpBrur7eybZIndQgcXCeZq&uniplatform=NZKPT&language=gb)
9. [基于ConvLSTM的南京地区共享单车需求预测研究](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7MkNxt7j_d_9JPlCh0YUlcMfNuXhrJq8MKy4WLOpDljV2ScK2ouMsd0-7rJUn0VyMJIJZmX_9NzfG6Q7qANHukzeDMQwgjsI0BPYQJoWVC1fKlwFDGD0Yaq&uniplatform=NZKPT&language=gb)
10. [天气及建成环境对共享单车出行需求的影响研究](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=wcPNn8Zia7Nl7v75OAN5S1L0ooZVB3zr5O-exXem7iYVK43mVNzhxIjgFyi77honMlkMnNDTAWTYyyxKu5URwcR_GitNwm7BR5G0zFtYjJkDnlcn8qA4s5Xq_57PPFjpEsOaI25w8gwmpzkt_zrZqA==&uniplatform=NZKPT&language=CHS)
11. [基于TRACLUS算法的船舶轨迹分析系统的设计与实现](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=IILC1c-FiAHvDk1rxNT-PZsg5zz9LaATLYpPM-rVLAVEUJCIs2bjT3Lsp5ETFip9wYuZygfIAsiPeBl1gIDJ8Sfj1hNF5xyd5nu0LIV1CkBDmqljoP6g8TY8ZJAJQiBCWUtgwtp_ydd3n_QdXobiBw==&uniplatform=NZKPT&language=CHS)


12. [基于GeoHash和HDBSCAN的共享单车停车拥挤区域识别](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=v5HVlYuqh9qu0R9T2MZidT__6Rt24c8X4D9foMZS_pzcQzuVcGVzX0IE-OjTOG-t2LTCcHl1eKQT6YGrO2QZtqx3XAqMgOq3EK5c-4rX3Am6oCHzvqQBylejH1kpZTLgpoj4jWQtnYGtA9uKzb8grQ==&uniplatform=NZKPT&language=CHS)
13. [GeoHash与KNN在共享单车停靠点优化选择中的应用](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=v5HVlYuqh9ogrb2hNXgm1-MENxnggnCX_--5mEMR9zSH-EqEqF79wFrNKjsOL3uVptNcDsSGosuCrj46wnIIfzYACxeaXLHRHgBQw_COWRk0jCsCr9CaIjVQKCSO_KU9zeIZt5Hrz66RnDNGPv-f0g==&uniplatform=NZKPT&language=CHS)
14. [基于GeoHash索引的A~*算法优化](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=v5HVlYuqh9qzdSQZLR_7MqrBP-Ru1lUKVJXVGtvotdssr8q8bZI8YFVZThmmKotEqVSH_sJxvoD11tF1eKfulzt7rXbzLzR0eQEx9ZjGH4ov57V0KD5Ia4IoSV4hO_lCBxW5YvG-ksmefmKL1EdqgA==&uniplatform=NZKPT&language=CHS)
15. [基于DBSCAN聚类和LSTM网络的装甲车辆集群轨迹预测方法](https://webvpn.sdust.edu.cn/https/77726476706e69737468656265737421fbf952d2243e635930068cb8/kcms2/article/abstract?v=v5HVlYuqh9qWE5Iy3HPsgrFFCONuM-N6Vr3XKA7xBygqSPrf8y4k9wCD3xJTzBg8F7YnoiOzlQFxzIBlVwwbQRRLzaDnX8_4aorslJD2hUXex5bTSKr7ksOZhwF-tt3_VRSguL-sHAs=&uniplatform=NZKPT&language=CHS)