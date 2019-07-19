class Solution:
    def numSquares(self, n):
        i, squareList = 1, []
        while i:
            tmp = i * i
            if tmp == n: return 1
            if tmp < n:
                squareList.append(tmp)
            else: break            
            i += 1
        total, sumList = 0, [n]
        while sumList: #BFS
            total += 1
            tmp = []
            for _sum in sumList:
                for _square in squareList:
                    if _sum == _square: return total
                    if _sum < _square: break
                    tmp.append(_sum - _square)
            sumList = tmp
        return total
