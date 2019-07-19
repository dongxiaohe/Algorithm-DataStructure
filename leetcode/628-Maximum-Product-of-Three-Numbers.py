class Solution(object):
    def maximumProduct(self, nums):
        _min1, _min2, _max1, _max2, _max3 = float("inf"), float("inf"), float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num > _max1:
                _max3 = _max2
                _max2 = _max1
                _max1 = num
            elif num > _max2:
                _max3 = _max2
                _max2 = num
            elif num > _max3:
                _max3 = num
            if num < _min1:
                _min2 = _min1
                _min1 = num
            elif num < _min2:
                _min2 = num
        return max(_max1 * _max2 * _max3, _min1 * _min2 * _max1)

