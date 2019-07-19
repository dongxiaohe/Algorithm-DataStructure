class Solution(object):
    def kClosest(self, points, K):
        distance = lambda i: points[i][0]**2 + points[i][1]**2
        def partition(i, j):
            start = i
            pivot = distance(start)
            i += 1
            while True:
                while i < j and distance(i) < pivot: i += 1
                while i <= j and distance(j) >= pivot: j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]
            points[start], points[j] = points[j], points[start]
            return j
        def quickSelect(i, j, K):
            if i >= j: return
            mid = partition(i, j)
            if K < mid + 1 - i: quickSelect(i, mid - 1, K)
            elif K > mid - i + 1: quickSelect(mid + 1, j, K - mid - 1 + i)
        quickSelect(0, len(points) - 1, K)
        return points[:K]
