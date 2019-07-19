"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

Leetcode Problem 41 https://leetcode.com/problems/first-missing-positive/

Put number into correct position in the list. 4 -> nums[3] 
"""
def firstMissingPositive(self, nums):
    n = len(nums)
    for i in range(n):
        while nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            k = nums[i] - 1
            nums[i], nums[k] = nums[k], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
