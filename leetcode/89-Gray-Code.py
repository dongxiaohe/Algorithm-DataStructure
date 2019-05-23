class Solution:
    def grayCode(self, n):
        return [i ^ (i >> 1) for i in range(0, 1 << n)] # it is a XOR operator between each and each / 2
    """
    0 => 00 ^ 00 => 00 => 0
    1 => 01 ^ 00 => 01 => 1
    2 => 10 ^ 00 => 11 => 3
    3 => 11 ^ 01 => 10 => 2
    """
