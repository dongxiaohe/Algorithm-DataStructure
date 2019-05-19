class Solution:
    def letterCombinations(self, digits):
        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        num = len(digits)
        for i in range(num):
            if i == 0: # or initialize empty string to remove this.
                for ele in table[digits[i]]:
                    result += ele
            else:
                tmp = []
                for t in result: 
                    for ele in table[digits[i]]:
                        tmp.append(t + ele)
                result = tmp
        return result
print(Solution().letterCombinations("267"))
