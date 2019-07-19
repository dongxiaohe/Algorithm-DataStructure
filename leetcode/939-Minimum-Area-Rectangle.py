class Solution(object):
    def minAreaRect(self, points):
        pointsSet = set(map(tuple, points))
        result = float("inf")
        for i, p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in pointsSet and (p2[0], p1[1]) in pointsSet:
                    result = min(result, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        return result if result != float("inf") else 0
