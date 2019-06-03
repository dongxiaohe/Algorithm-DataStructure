class Solution:
    def _isPal(self, s): return s == s[::-1]
    def partition(self, s):
        if not s: return []
        result = []
        """
        This logic is to check s itself is a palindrome
        """
        if self._isPal(s):
            result.append([s])
        """
        This is a super cool way to do the backtracking. i.e. [1,2,3] => num: 2 ^ 2 [[1], [2], [3]], [[1, 2], [3]], [[1, 2, 3]], [[1], [2, 3]]
        Pseudo code:
            result = []
            for i in range(1, len(s)):
                head = s[0:i]
                tails = partition(s[i:])
                if len(tails) > 0:
                    for each in tails:
                        result.append([head] + each)
            return result 
        """
        for i in range(1, len(s)):
            start = s[0:i]
            if self._isPal(start):
                rest = self.partition(s[i:])
                if len(rest) > 0:
                    for each in rest:
                        result.append([start] + each)
        return result
                
Solution().partition([1,2,3,4, 5])
Solution().partition([1,1,1])

