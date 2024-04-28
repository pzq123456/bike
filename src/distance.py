from typing import List
import pygeohash as pgh
import math

# 曼哈顿距离
def manhattan(p1: List[float], p2: List[float]) -> float:
    return sum([abs(p1[i]-p2[i]) for i in range(len(p1))])

def encode(lat: float, lon: float) -> str:
    return pgh.encode(lat, lon)

def decode(geohash: str) -> List[float]:
    # return pgh.decode(geohash)
    # 交换经纬度
    return list(pgh.decode(geohash)[::-1])

def geohash_approximate_distance(geohash1: str, geohash2: str) -> int:
    return pgh.geohash_approximate_distance(geohash1, geohash2)

def haversine(latlng1: List[float], latlng2: List[float], R: float = 6378137.0) -> float:
    rad = math.pi / 180
    lat1 = latlng1[0] * rad
    lat2 = latlng2[0] * rad
    sinDLat = math.sin((latlng2[0] - latlng1[0]) * rad / 2)
    sinDLon = math.sin((latlng2[1] - latlng1[1]) * rad / 2)
    a = sinDLat * sinDLat + math.cos(lat1) * math.cos(lat2) * sinDLon * sinDLon
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# test haveisine
# print(haversine([31.359,121.412],[31.359,121.413])) # 0.001

# test code
# print(encode(31.359,121.413)) # >>> 'wtw66u9x2tkc'


# print(pgh.encode(31.359,121.413)) 

# print(pgh.decode('wtw66u9x2tkc')) # >>> (‘42.6’, ‘-5.6’)

# print(pgh.geohash_approximate_distance('wtw66u9x2tkc', 'wtw66udprvq3')) # >>> 625441
# test code
# print(manhattan([121.412,31.359],[121.413,31.359])) # 0.001
