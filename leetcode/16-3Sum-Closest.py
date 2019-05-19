class Solution:
    def threeSumClosest(self, nums, target):
        result = float("inf")
        nums.sort()
        l = len(nums)
        for i in range(l - 1):
            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = l - 1
                while left < right:
                    total = nums[i] + nums[left] + nums[right]
                    distance = target - total                    
                    if distance == 0:
                        return target
                    elif distance < 0:
                        right -= 1
                    elif distance > 0:
                        left += 1
                    if abs(distance) < abs(target - result):
                        result = total
        return result
print(Solution().threeSumClosest([-1, 2, 1, -4], 1))                    
