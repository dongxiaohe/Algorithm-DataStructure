class Solution:
    def maxArea(self, height):
        j = len(height) - 1
        i = 0
        result = 0
        while i < j:
            total = min(height[i], height[j]) * (j - i) 
            if total > result:
                result = total
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return result
