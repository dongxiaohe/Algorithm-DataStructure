class Solution(object):
    def diStringMatch(self, S):
        low, high = 0, len(S)
        result = []
        for ch in S:
            if ch == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        return result + [high]

