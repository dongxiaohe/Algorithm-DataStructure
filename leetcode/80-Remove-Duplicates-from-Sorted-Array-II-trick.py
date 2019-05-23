class Solution:
    def removeDuplicates(self, nums):
        i = 0 
        # pretty good in place trick
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        nums[i:] = []

t = [1,1,1,2,2,2,3,3] 
Solution().removeDuplicates(t)
print(t)
