from preprocess import save_track,load_track
# 提取一辆单车在一个月内的流动情况
# ID,BID,UID,ST,SX,SY,ET,EX,EY,EC,DS,DU
# 1,79699,759,2016/8/1 0:23,121.52,31.309,2016/8/1 0:32,121.525,31.316,3,867.65,9

# BID 代表单车编号 按照时间串联某一单车在一个月内的轨迹 SX,SY -> EX,EY -> SX,SY
# 以单车编号为索引，提取单车在一个月内的轨迹数据 