from geopy.distance import geodesic
from geographiclib.geodesic import Geodesic

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Distance(self, other):
        return geodesic((self.x, self.y), (other.x, other.y)).meters
    

# ヘロンの公式
def triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

def PolygonArea(v):
    if len(v) < 3:  #3点以下は三角形にならない
        return [0]

    sum = 0
    v0 = v[0]
    for i in range(1, len(v) - 1):
        v1 = v[i]
        v2 = v[i + 1]
        v1_v0 = v1.Distance(v0)
        v2_v0 = v2.Distance(v0)
        v1_v2 = v1.Distance(v2)
        a = triangle_area(v1_v0, v2_v0, v1_v2)
        sum += a

    return abs(sum)

# 頂点の緯度経度
points = [
    Point(35.664338, 139.637408),
    Point(35.664299, 139.637977),
    Point(35.664750, 139.638041),
    Point(35.664658, 139.638792),
    Point(35.665500, 139.638829),
    Point(35.665049, 139.637610)
    # 他の頂点を追加
]

# 三角形の各辺の長さを求め、面積を計算
polygon_area = PolygonArea(points)

print("面積は {:.2f} 平方メートルです。".format(polygon_area))
