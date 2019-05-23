class Solution:
    def addBinary(self, a, b):
        i, j, carry, result = len(a) - 1, len(b) - 1, 0, collections.deque()
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += int(a[i])
                i -= 1
            if j >= 0:
                _sum += int(b[j])
                j -= 1
            result.appendleft(str(_sum % 2))
            carry = _sum // 2
        if carry: result.appendleft(str(carry))
        return "".join(result)
