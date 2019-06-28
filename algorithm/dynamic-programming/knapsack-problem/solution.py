"""
Given items' weights[] and values[], return max value for particular capacity
Weights = [10, 20, 30]
Values = [60, 100, 120]
Capacity = 50
"""
def solution(weights, values, capacity):
    row, column = len(weights), capacity + 1
    dp = [[0 for _ in range(column)] for _ in range(row)]
    for i in range(row):
        for j in range(1, column):
            if i == 0:
                if j >= weights[i]:
                    dp[i][j] = values[i]
            else:
                diff = j - weights[i]
                if diff >= 0:
                    dp[i][j] = max(values[i] + dp[i - 1][diff], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
    return dp[row - 1][column - 1]

print(solution([10, 20, 30], [60, 100, 120], 50))
print(solution([1, 3, 4, 5], [1, 4, 5, 7], 7))

