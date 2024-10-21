# The Documents for the project

## Algorithms

### Algorithm 1 - GPS Trajectory Reconstruction

#### 1.1 Reordering Algorithm
核心概念 最近的点大概率是下一个点

key Concept: The nearest point is probably the next point

性能如何？详细实现？

How about the performance? Detailed implementation?

初始化：计算轨迹点GeoHash并存入集合（S）；取出轨迹起点放入结果列表（L）

Initialization: Calculate the GeoHash of the trajectory point and store it in the set (S); take out the starting point of the trajectory and put it into the result list (L)

整理格式，输出结果

Format the data and output the result

我们有差不多十万条轨迹记录，想要高效地开展研究，就不得不考虑算法的性能问题。

We have almost 100,000 trajectory records and want to carry out research efficiently, so we have to consider the performance of the algorithm.

set 数据结构可以帮助我们实现去重。但是会导致坐标精度损失，也就无法保证点的唯一性。

The set data structure can help us achieve deduplication. But it will lead to coordinate precision loss, which means that the uniqueness of the point cannot be guaranteed.

欧氏距离涉及到开方运算，计算量较大。可以使用曼哈顿距离优化

Euclidean distance involves square root operation, which has a large amount of calculation. can be optimized using Manhattan distance

在中央处理器为 i7-10870H，机带RAM 16GB 的 Windows11 笔记本上，使用该算法处理十万条轨迹数据总耗时约1小时31分。

On a Windows11 notebook with a central processor of i7-10870H and a machine with 16GB of RAM, it takes about 1 hour and 31 minutes to process 100,000 trajectory data using this algorithm.

算法副作用：顺带计算了每一个轨迹的长度

Side effect of the algorithm: Calculated the length of each trajectory

#### 1.2 Simplification Algorithm
原始轨迹数据由于定位设备的限制，存在大量冗余点及锯齿状噪声。

Due to the limitations of the positioning device, the original trajectory data contains a large number of redundant points and jagged noise.

对重排序后的轨迹数据进行阈值为0.0015的道格拉斯-普克抽稀操作。

Douglas-Peucker simplification operation with a threshold of 0.0015 on the reordered trajectory data.

取轨迹终点作为当前点（c），计算其GeoHash值，作为查询字符转（cstr）

Get the end point of the trajectory as the current point (c), calculate its GeoHash value, and use it as the query character string (cstr)

去除cstr最后一位

Remove the last character of cstr

查询对应兴趣点类别编码，并返回结果

Query the corresponding interest point category code and return the result

### Algorithm 2 - Road Network Matching
### Algorithm 3 - POI Matching

骑行数据仅仅包含了经纬度信息，缺乏对骑行目的地类别的直接标注，这限制了对骑行行为的深入分析。

The riding data only contains latitude and longitude information, lacking direct labeling of the destination category, which limits the in-depth analysis of riding behavior.

The First Law of Geography, according to Waldo Tobler, is "everything is related to everything else, but near things are more related than distant things."

初始化：依次计算所有兴趣点的GeoHash值并插入前缀索引树（T）

Initialization: Calculate the GeoHash value of all interest points in turn and insert them into the prefix index tree (T)

| 类名 | 英文名 | 编码 |
| -- | -- | -- |
| 交通设施服务 | Transportation | 0 |
| 体育休闲服务 | Sports and Leisure | 1 |
| 公司企业 | Company | 2 |
| 商务住宅 | Business Residence | 3 |
| 科教文化服务 | Science and Education Culture | 4 |
| 购物服务 | Shopping | 5 |
| 风景名胜 | Scenic Spots | 6 |
| 餐饮服务 | Catering | 7 |

据本机（i7-10870H,RAM 16 GB）测算，执行一次 haversine 算法大约消耗 15 μs，粗略估计，在不考虑排序操作的情况下，算法将执行超过三小时，因此需要建立用于支持高效查找的空间数据结构。

According to the test on this machine (i7-10870H, RAM 16 GB), executing the haversine algorithm consumes about 15 μs. Roughly estimated, the algorithm will take more than three hours to execute

高效的空间索引大大加快了最邻近查找的速度，经试验，在十二万条兴趣点数据集中使用该算法对近十万条轨迹数据的终点进行最邻近匹配共耗费约两分钟。

Efficient spatial indexing greatly speeds up the speed of nearest neighbor search. After the experiment, using this algorithm to match the end points of nearly 100,000 trajectory data in a dataset of 120,000 interest points took about two minutes.

https://learn.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system


### Algorithm 4 - Tide Analysis

现考虑研究区域内的某一有限大小区域，在某一时段内的单车借还情况，并定义潮汐指数（Tide Index, TI）为：

Now consider a limited area in the research area, the situation of borrowing and returning a single car in a certain period of time, and define the tide index (Tide Index, TI) as:

$$ TI = \frac{Borrow - Return}{Borrow + Return} $$

其中，Borrow为某一时段内该区域的借车数量，Return为某一时段内该区域的还车数量。潮汐指数为正值时，表示该区域为借车潮汐点，即借车需求大于还车需求；潮汐指数为负值时，表示该区域为还车潮汐点，即还车需求大于借车需求。潮汐指数的绝对值越大，说明潮汐现象越明显，即借还失衡程度越大。

| TI | Meaning |
| -- | -- |
| TI > 0 | Borrowing rqeuirement is greater than returning requirement |
| TI < 0 | Returning requirement is greater than borrowing requirement |

## 分析
### 时间上

1. 骑行时距总体分布：绘制骑行时距总体分布直方图，分析骑行时距的分布规律。
2. 工作日骑行订单量分布：以一周七个工作日为分组依据，绘制工作日骑行订单量分布直方图，分析工作日骑行订单量的分布规律。
3. 两次骑行间隔时间分布：计算同一用户两次骑行之间的间隔时间，绘制时间间隔概率密度分布曲线。

4. Distribution of riding time: Draw a histogram of the distribution of riding time and analyze the distribution law of riding time.
5. Distribution of riding orders on working days: Grouped by seven working days a week, draw a histogram of the distribution of riding orders on working days, and analyze the distribution law of riding orders on working days.
6. Distribution of time interval between two rides: Calculate the time interval between two rides of the same user and draw the probability density distribution curve of the time interval.


### 空间上

1. 骑行目的地类别分布：绘制骑行目的地类别分布饼图，分析骑行目的地类别的分布规律。
2. 骑行道路匹配分析：对骑行轨迹进行道路匹配，统计骑行轨迹的道路匹配情况。（Zeng）
3. 潮汐现象分析：分析骑行轨迹的潮汐现象，即骑行轨迹的起点与终点的分布规律。

1. Distribution of riding destination categories: Draw a pie chart of the distribution of riding destination categories and analyze the distribution law of riding destination categories.
2. Riding road matching analysis: Match the riding trajectory to the road and count the road matching of the riding trajectory.
3. Tide analysis: Analyze the tide phenomenon of riding trajectory, that is, the distribution law of the starting point and end point of riding trajectory.