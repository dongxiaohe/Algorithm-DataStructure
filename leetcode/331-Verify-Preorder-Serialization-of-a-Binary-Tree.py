class Solution:
    def isValidSerialization(self, preorder):
        diff = 1
        for t in preorder.split(","):
            diff -= 1
            if diff < 0: return False
            if t != "#": diff += 2
        return diff == 0

