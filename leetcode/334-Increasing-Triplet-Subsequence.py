class Solution:
    def increasingTriplet(self, nums):
        first = second = float("inf")
        for t in nums:
            if t <= first: first = t # two classic guards
            elif t <= second: second = t
            else: return True
        return False

