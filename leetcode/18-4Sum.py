class Solution:
    def fourSum(self, nums, target):
        l = len(nums)
        if l < 4: return []
        nums.sort()
        result = []
        for i in range(l - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(i + 1, l - 1):
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        left = j + 1
                        right = l - 1
                        while left < right:
                            total = nums[i] + nums[j] + nums[left] + nums[right]
                            if total == target:
                                result.append([nums[i], nums[j], nums[left], nums[right]])
                                while left < right and nums[left] == nums[left + 1]:
                                    left += 1
                                while left < right and nums[right] == nums[right - 1]:
                                    right -= 1
                                left += 1
                                right -= 1
                            elif total < target:
                                left += 1
                            else:
                                right -= 1
        return result
