import math


A = 6378137.0
MAXEXTENT = 20037508.342789244
MAXLAT = 85.05112877980659

def project(lonlat):
    d = math.pi / 180
    max = MAXLAT
    lat = lonlat[1]
    if lat > max: lat = max
    if lat < -max: lat = -max
    sin = math.sin(lat * d)

    x = A * lonlat[0] * d
    y = A * math.log((1 + sin) / (1 - sin)) / 2

    if y > MAXEXTENT: y = MAXEXTENT
    if y < -MAXEXTENT: y = -MAXEXTENT
    if x > MAXEXTENT: x = MAXEXTENT
    if x < -MAXEXTENT: x = -MAXEXTENT

    return [x, y]

def unproject(point):
    d = 180 / math.pi
    return [point[0] * d / A, (2 * math.atan(math.exp(point[1] / A)) - math.pi / 2) * d]

def project_list(lst):
    return [project(i) for i in lst]