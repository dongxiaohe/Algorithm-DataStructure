class Solution:
    def numDecodings(self, s):
        if not s: return 0
        pTotal, cTotal, p = 0, 1 if s[0] != 0 else 0, ''
        for c in s:
            """
              i.e   1,           1,                             1
                    1,   (1 * 1) + (1 * 0),             (2 * 1) + (1 * 1)

                    3,           0,                             3
                    1,   (1 * 1) + (0 * 0),             (1 * 1) + (0 * 1)                   
            """
            pTotal, cTotal, p = cTotal, (c > '0') * cTotal + (9 < int(p + c) < 27) * pTotal, c
        return cTotal

