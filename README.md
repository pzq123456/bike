# 基于共享单车骑行数据的上海市通勤模式分析(Shanghai Commuting Patterns Unveiled through Shared Bicycle Data)

## 文件结构
1. [data/](./data/) 数据及中间结果
2. [drawio/](./drawio/) 流程图及其绘制文件(*.drawio)
3. [paper/](./paper/) 论文正文 MarkDown 格式
4. [scripts/](./scripts/) JavaScript 代码（例如 GEE 平台代码）
5. [src/](./src/) Python 代码主要包括数据处理及（部分）绘图代码
6. [test/](./test/) 测试代码 用于测试部分自行封装的 Python 函数
7. [word/](./word/) 论文 word 版及其他需要上交的资料

## 目录
- [x] [第一章 绪论](./paper/chapters/c1.md)
- [x] [第二章 理论基础与相关技术](./paper/chapters/c2.md)
- [x] [第三章 研究数据与方法](./paper/chapters/c3.md)
- [x] [第四章 结果与讨论](./paper/chapters/c4.md)
- [x] [第五章 总结与展望](./paper/chapters/c5.md)
- [x] [附录](./paper/chapters/c6.md)
- [x] [致谢](./paper/chapters/c7.md)

## Refernces
1. [1]Shaheen, S. A., Guzman, S., & Zhang, H. (2010). Bikesharing in Europe, the Americas, and Asia: Past, Present, and Future[J]. Transportation Research Record, 2143(1), 159-167. https://doi.org/10.3141/2143-20
2. [2]Elliot Fishman, Simon Washington, Narelle Haworth, Armando Mazzei. 2014. Barriers to bikesharing: an analysis from Melbourne and Brisbane[J]. Journal of Transport Geography,Volume 41,Pages 325-337,ISSN 0966-6923,https://doi.org/10.1016/j.jtrangeo.2014.08.005.
3. [3]Zhang, H., Shaheen, S. A., & Chen, X. 2014. Bicycle Evolution in China: From the 1900s to the Present[J]. International Journal of Sustainable Transportation, 8(5), 317–335. https://doi.org/10.1080/15568318.2012.699999
4. [4]全雨霏. 南京市共享单车使用的时空特征及其骑行环境评估[D].东南大学,2024.DOI:10.27014/d.cnki.gdnau.2022.001097.
5. [5]Jonathan Corcoran, Tiebei Li, David Rohde, Elin Charles-Edwards, Derlie Mateo-Babiano. 2014. Spatio-temporal patterns of a Public Bicycle Sharing Program: the effect of weather and calendar events[J]. Journal of Transport Geography,Volume 41,Pages 292-305,ISSN 0966-6923,https://doi.org/10.1016/j.jtrangeo.2014.09.003.
6. [6]Yang Xu, Dachi Chen, Xiaohu Zhang, Wei Tu, Yuanyang Chen, Yu Shen, Carlo Ratti.Unravel the landscape and pulses of cycling activities from a dockless bike-sharing system[J]. Computers, Environment and Urban Systems, Volume 75, 2019,Pages 184-203, DOI:https://doi.org/10.1016/j.compenvurbsys.2019.02.002.
7. [7]杨永崇,柳莹,李梁.利用共享单车大数据的城市骑行热点范围提取[J].测绘通报,2018(08):68-73.DOI:10.13474/j.cnki.11-2246.2018.0247.
8. [8]高楹,宋辞,舒华,等.北京市摩拜共享单车源汇时空特征分析及空间调度[J].地球信息科学学报,2018,20(08):1123-1138.
9. [9]王若萱,吴建平,奇格奇. 基于上海市数据的共享单车用户通勤模式研究（英文）[C]中国仿真学会.第三十三届中国仿真大会论文集.2021:16.DOI:10.26914/c.cnkihy.2021.025005.
10. [10]Pilar Jiménez, María Nogal, Brian Caulfield, Francesco Pilla. 2016. Perceptually important points of mobility patterns to characterise bike sharing systems: The Dublin case[J]. Journal of Transport Geography, Volume 54, Pages 228-239, ISSN 0966-6923, https://doi.org/10.1016/j.jtrangeo.2016.06.010.
11. [11]张芳,陈彬,汤杨华,等.基于兴趣点聚类的无桩共享单车时空模式分析[J].系统仿真学报,2019,31(12):2829-2836.DOI:10.16182/j.issn1004731x.joss.19-FZ0327.
12. [12]刘冰,王舸洋,朱俊宇,等.基于共享单车大数据的骑行生活圈识别及其活动网络模式分析[J].城市规划学刊,2023(04):32-40.DOI:10.16361/j.upf.202304005.
13. [13]常新. 基于共享单车轨迹数据的城市街道可骑行性研究[D].哈尔滨工业大学,2021.DOI:10.27061/d.cnki.ghgdu.2020.002483.
14. [14]谢国微. 天气及建成环境对共享单车出行需求的影响研究[D].南京林业大学,2024.DOI:10.27242/d.cnki.gnjlu.2022.000493.
15. [15]高枫,李少英,吴志峰,等.广州市主城区共享单车骑行目的地时空特征与影响因素[J].地理研究,2019,38(12):2859-2872.
16. [16]Shen, Y., Zhang, X., & Zhao, J[J]. 2018. Understanding the usage of dockless bike sharing in Singapore. International Journal of Sustainable Transportation, 12(9), 686-700.
17. [17]谢光明. 基于改进时空图神经网络的共享单车流量预测[D].华东师范大学,2023.DOI:10.27149/d.cnki.ghdsu.2023.004430.
18. [18]Jie Bao, Tianfu He, Sijie Ruan , Yanhua Li, and Yu Zheng. 2017. Planning Bike Lanes based on Sharing-Bikes’ Trajectories[C]. In Proceedings of KDD’17, August 13–17, 2017, Halifax, NS, Canada., , 11 pages.
19. [19]王俊,于爱荣.基于ConvLSTM的南京地区共享单车需求预测研究[J].软件工程,2024,27(02):55-59.DOI:10.19644/j.cnki.issn2096-1472.2024.002.011.
20. [20]李文翔,唐桂孔,刘博,等.基于摩拜骑行数据的上海市共享单车减排效益时空分析[J].环境科学学报,2021,41(11):4752-4759.DOI:10.13671/j.hjkxxb.2021.0213.
21. [21]刘泉宏,唐福星.基于K-means聚类算法与重心法的故障共享单车回收中心选址优化[J].运筹与管理,2023,32(07):85-91.
22. [22]任丹. 基于TRACLUS算法的船舶轨迹分析系统的设计与实现[D].辽宁师范大学,2021.DOI:10.27212/d.cnki.glnsu.2020.001211.
23. [23]塔娜,柴彦威.行为地理学的学科定位与前沿方向[J].地理科学进展,2022,41(01):1-15.
24. [24]张文佳,鲁大铭.行为地理学的方法论与微观人地关系研究范式[J].地理科学进展,2022,41(01):27-39.
25. [25]杨超,汪超.城市过剩通勤与职住平衡模型[J].同济大学学报(自然科学版),2013,41(11):1712-1716.
26. [26]岳丽莹. 超大城市职住关系与通勤绩效研究[D].华东师范大学,2022.DOI:10.27149/d.cnki.ghdsu.2022.000593.
27. [27]刘望保,闫小培,方远平,等.广州市过剩通勤的相关特征及其形成机制[J].地理学报,2008(10):1085-1096.
28. [28]龚玺,裴韬,孙嘉,等.时空轨迹聚类方法研究进展[J].地理科学进展,2011,30(05):522-534.
29. [29]夏琼燕,罗冠,张翔,等.OpenStreetMap志愿者贡献与留存分析[J].测绘与空间地理信息,2021,44(02):90-93+97.
30. [30]赵雨琪,牟乃夏,祝帅兵,等.基于GeoHash算法的周边查询应用研究[J].软件导刊,2016,15(06):16-18.