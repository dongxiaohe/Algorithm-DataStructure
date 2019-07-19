"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

Leetcode problem 238 https://leetcode.com/problems/product-of-array-except-self/
"""
def productExceptSelf(self, nums):
    left, right, size = 1, 1, len(nums)
    result = [1] * size
    for i in range(1, size):
        result[i] = result[i - 1] * nums[i - 1]
    for i in range(size - 1, -1 , -1):
        result[i] *= right
        right *= nums[i]
    return result

print(productExceptSelf([1, 2, 3, 4, 5]))
