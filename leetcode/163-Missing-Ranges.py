class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        result = []
        nums.append(upper + 1)
        pre = lower - 1
        for number in nums:
            if number == pre + 2: result.append(str(number - 1))
            elif number > pre + 2: result.append(str(pre + 1) + "->" + str(number - 1))
            pre = number
        return result
