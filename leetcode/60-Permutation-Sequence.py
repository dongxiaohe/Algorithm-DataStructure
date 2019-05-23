class Solution:
    def getPermutation(self, n, k):
        numbers, factorial, sum, result = list(range(1, n + 1)), [1, 1], 1, ""
        k -= 1
        for i in range(2, n):
            sum *= i
            factorial.append(sum)
        for i in range(1, n + 1):
            index = k // factorial[n - i]
            result += str(numbers[index])
            numbers.pop(index)
            k -= index * factorial[n - i]
        return result
print(Solution().getPermutation(3, 3))
print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(8, 15485 ))
