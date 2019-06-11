class Solution(object):
    def numTilePossibilities(self, tiles):
        def backtrack(count):
            acc = 0
            for i in range(26):
                if count[i] == 0: continue
                acc += 1
                count[i] -= 1
                acc += backtrack(count)
                count[i] += 1
            return acc
        count = [0 for _ in range(26)]
        for ch in tiles:
            count[ord(ch) - ord('A')] += 1
        return backtrack(count)
