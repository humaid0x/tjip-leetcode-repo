from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, qpoint: List[int]) -> int:
        res = 0
        x2 = qpoint[0]
        y2 = qpoint[1]

        for point in self.points:
            x4, y4 = point
            if x2 == x4 or abs(x2 - x4) != abs(y2 - y4):
                continue
                
            if self.points.get((x4, y2)) and self.points.get((x2, y4)):
                res += self.points.get((x4, y2)) \
                    * self.points.get((x2, y4)) \
                    * self.points.get((x4, y4))

        return res
		