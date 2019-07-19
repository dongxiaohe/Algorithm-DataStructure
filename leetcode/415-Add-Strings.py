class Solution(object):
    def addStrings(self, num1, num2):
        i, j, carry, deque, _sum = len(num1) - 1, len(num2) - 1, 0, collections.deque(), 0
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += int(num1[i])
                i -= 1
            if j >= 0:
                _sum += int(num2[j])
                j -= 1
            deque.appendleft(str(_sum % 10))
            carry = _sum // 10
        if carry: deque.appendleft("1")
        return "".join(deque)
