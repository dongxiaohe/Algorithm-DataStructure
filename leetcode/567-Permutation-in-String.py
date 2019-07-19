class Solution(object):
    def checkInclusion(self, s1, s2):
        def index(ch): return ord(ch) - ord("a")
        expected = [0 for _ in range(26)]
        for ch in s1:
            expected[index(ch)] += 1
        chCount = [0] * 26
        window = len(s1)
        for i, ch in enumerate(s2):
            chCount[index(ch)] += 1
            if i >= window:
                chCount[index(s2[i - window])] -= 1
            if chCount == expected: return True
        return False

