class FenwickTree:
    def __init__(self, nums):
        self._sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])
    def update(self, i, delta):
        i += 1
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & (-i)
    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & (-i)
        return s

class NumArray:
    def __init__(self, nums):
        self.fenwickTree = FenwickTree(nums)
        self.nums = nums
        print(self.fenwickTree._sums)

    def update(self, i, val):
        delta = val - self.nums[i]
        self.nums[i] = val
        self.fenwickTree.update(i, delta)

    def sumRange(self, i, j):
        return self.fenwickTree.query(j) - self.fenwickTree.query(i - 1)


