class Solution(object):
    def totalFruit(self, tree):
        numberMap = collections.defaultdict(int)
        missing, i, result = 2, 0, 0
        for j, number in enumerate(tree):
            numberMap[number] += 1
            if numberMap[number] == 1: missing -= 1
            while missing < 0:
                numberMap[tree[i]] -= 1
                if numberMap[tree[i]] == 0: missing += 1
                i += 1
            result = max(result, j - i + 1)
        return result
