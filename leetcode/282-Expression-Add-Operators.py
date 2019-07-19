class Solution(object):
    def addOperators(self, num, target):
        def backtrack(arr, index, pre, cur, value, target, acc, result):
            if index == len(arr):
                if value == target and cur == 0: result.append(acc[1:])
                return
            cur = cur * 10 + arr[index]
            if cur > 0:
                backtrack(arr, index + 1, pre, cur, value, target, acc, result)
            backtrack(arr, index + 1, cur, 0, value + cur, target, acc + "+" + str(cur), result)
            if acc:
                backtrack(arr, index + 1, -cur, 0, value - cur, target, acc + "-" + str(cur), result)
                backtrack(arr, index + 1, cur * pre, 0, value - pre + (pre * cur), target, acc + "*" + str(cur), result)
        if not num: return []
        result = []
        arr = list(map(lambda x: int(x), list(num)))
        backtrack(arr, 0, 0, 0, 0, target, "", result)
        return result


