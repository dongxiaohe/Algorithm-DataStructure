class Solution(object):
    def oddEvenJumps(self, A):
        n = len(A)
        higher, lower = [False] * n, [False] * n
        higher[n - 1] = lower[n - 1] = True
        val_map = {}
        val_map[A[n - 1]] = n - 1
        sorted_vals = [A[n - 1]]
        result = 1
        for i in range(n - 2, -1, -1):
            if A[i] in val_map:
                higher[i] = lower[val_map[A[i]]]
                lower[i] = higher[val_map[A[i]]]
            else:
                index = bisect.bisect(sorted_vals, A[i])
                if index != len(sorted_vals):
                    higher[i] = lower[val_map[sorted_vals[index]]]
                if index != 0:
                    lower[i] = higher[val_map[sorted_vals[index - 1]]]
                bisect.insort(sorted_vals, A[i])
            if higher[i]: result += 1
            val_map[A[i]] = i
        return result
