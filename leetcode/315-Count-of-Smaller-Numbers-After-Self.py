class Solution(object):
    def countSmaller(self, nums):
        result, seen = [], []
        for num in nums[::-1]:
            position = bisect.bisect_left(seen, num)
            result.append(position)
            bisect.insort(seen, num)
        result.reverse()
        return result
