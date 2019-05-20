class Solution:
    def trap(self, height):
        left, right, maxLeft, maxRight, result = 0, len(height) - 1, 0, 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft: maxLeft = height[left]
                else: result += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight: maxRight = height[right]
                else: result += maxRight- height[right]
                right -= 1
        return result

# print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(Solution().trap([2,0,2]))
# print(Solution().trap([1,3,4]))