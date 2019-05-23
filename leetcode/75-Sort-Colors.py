class Solution:
    def sortColors(self, nums):
        countState = {}
        for num in nums:
            if num in countState:
                countState[num] += 1
            else: countState[num] = 1
        sortedKeys = sorted(countState.keys())
        i, n = 0, len(nums)
        while i < n:
            key = sortedKeys[0] 
            if key in countState and countState[key] > 0:
                nums[i] = key
                countState[key] -= 1
                i += 1
            else: 
                sortedKeys.pop(0)

t = [2,0,2,1,1,0]
Solution().sortColors(t)
print(t)
