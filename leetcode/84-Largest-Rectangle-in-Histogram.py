class Solution:
    def largestRectangleArea(self, heights):
        stack, maxArea = [-1], 0
        heights.append(0) # the trick to trigger calculation 
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] # classic, we only calculate if j pointer value is bigger than i pointer value
                maxArea = max(maxArea, w * h)
            stack.append(i)
        return maxArea

print(Solution().largestRectangleArea([2,1,6,5,2,3]))
print(Solution().largestRectangleArea([2,1,5,6,2,3]))

