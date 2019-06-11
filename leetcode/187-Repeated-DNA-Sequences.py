class Solution:
    def findRepeatedDnaSequences(self, s):
        n, seen, repeated = len(s), {}, set()
        for i in range(n - 9):
            ten = s[i: i + 10]
            if ten in seen: repeated.add(ten)
            seen[ten] = True
        return list(repeated)
        
