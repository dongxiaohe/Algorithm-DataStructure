class Solution:
    def lengthOfLastWord(self, s):
        counter, n = 0, len(s)
        j = n - 1
        while j >= 0:
            if s[j] == ' ' and counter > 0: return counter
            elif s[j] != ' ': 
                counter += 1
            j -= 1
        return counter
