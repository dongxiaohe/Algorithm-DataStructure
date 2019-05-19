class Solution:
    def letterCombinations(self, digits):
        import functools
        if len(digits) == 0:
            return []
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
        reduceFunc = lambda acc, digit: [x + y for x in acc for y in table[digit]]
        return functools.reduce(reduceFunc, digits, [""]) 
