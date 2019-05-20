class Solution:
    def multiply(self, num1, num2):
        m, n = len(num1), len(num2)
        pos = [0 for _ in range(m + n)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j])
                # position p1 = i + j, p2 = i + j + 1
                p1, p2 = i + j, i + j + 1
                sum = tmp + pos[p2]
                pos[p1] += int(sum / 10)
                pos[p2] = int(sum % 10)
        result = ""
        for digit in pos:
            if len(result) != 0 or int(digit) != 0:
                result += str(digit)
        return result if len(result) != 0 else "0" 
