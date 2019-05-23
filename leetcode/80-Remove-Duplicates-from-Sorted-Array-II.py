class Solution:
    def removeDuplicates(self, nums):
        low, high = 0, len(nums) 
        while low < high:
            print(low, nums, high)
            if low + 1 < high and nums[low] == nums[low + 1]:
                counter = low + 2 
                while counter < high and nums[counter] == nums[low]:
                    print("here")
                    counter += 1
                if counter > low + 2:
                    nums[low + 2:] = nums[counter:]
                    high -= counter - (low + 2)
                else: low += 2
            else:
                low += 1
t = [1,1,1,2,2,2,3,3]
Solution().removeDuplicates(t)
print(t)

