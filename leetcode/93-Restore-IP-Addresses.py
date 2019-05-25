class Solution:
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12: return []
        def backtrack(s, start, acc, result):
            if len(acc) > 4: return
            if len(acc) == 4 and start == len(s):
                result.append(".".join(acc))
                return
            for step in range(1, 4):
                if start + step > len(s): break
                tmpStr = s[start: start + step]
                if (tmpStr.startswith("0") and len(tmpStr) > 1) or (step == 3 and int(tmpStr) >= 256): break
                backtrack(s, start + step, acc + [tmpStr], result)
        result = []
        backtrack(s, 0, [], result)
        return result
