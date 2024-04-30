import math
from typing import List
import time

def haversine(latlng1: List[float], latlng2: List[float], R: float = 6378137.0) -> float:
    rad = math.pi / 180
    lat1 = latlng1[0] * rad
    lat2 = latlng2[0] * rad
    sinDLat = math.sin((latlng2[0] - latlng1[0]) * rad / 2)
    sinDLon = math.sin((latlng2[1] - latlng1[1]) * rad / 2)
    a = sinDLat * sinDLat + math.cos(lat1) * math.cos(lat2) * sinDLon * sinDLon
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# 秒 的单位转换
def time_convert(seconds: float) -> str:
    if seconds < 1e-6:
        return f"{seconds * 1e9:.2f} ns"
    if seconds < 1e-3:
        return f"{seconds * 1e6:.2f} μs"
    if seconds < 1:
        return f"{seconds * 1e3:.2f} ms"
    return f"{seconds:.2f} s"

# 实现一个量测函数运行时间的装饰器
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        # print(f"Function {func.__name__} took {end - start} seconds")
        print(f"Function {func.__name__} took {time_convert(end - start)}")
        return result
    return wrapper




if __name__ == "__main__":
    # 测试装饰器
    @measure_time
    def test():
        haversine([31.22, 121.48], [39.93, 116.40])

    test()