class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        heights, maxArea = [0] * (n + 1), 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            stack = [-1]
            print(heights)
            for i in range(n + 1):    
                while heights[i] < heights[stack[-1]]:
                    print(i, stack[-1], stack) # classic, this can convert to maximun rectangles in histogram problems
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    maxArea = max(maxArea, h * w)
                stack.append(i)
        return maxArea

t = [
  ["1","0","0","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

print(Solution().maximalRectangle(t))
