class Comparable:
    def __init__(self, value):
        self.value = str(value)
    def __lt__(self, other):
        return self.value + other.value > other.value + self.value
    def __gt__(self, other):
        return self.value + other.value < other.value + self.value
    def __eq__(self, other):
        return self.value + other.value == other.value + self.value

class Solution:
    def largestNumber(self, nums):
        numsStr = [Comparable(x) for x in nums]
        numsStr.sort()
        result = "".join([x.value for x in numsStr])
        return result.lstrip("0") or "0
