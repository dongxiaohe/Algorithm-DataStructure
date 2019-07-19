class Solution(object):
    def isStrobogrammatic(self, num):
        kv = {"1": "1", "6": "9", "9": "6", "0": "0", "8": "8"}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in kv or num[right] not in kv or kv[num[left]] != num[right] or num[left] != kv[num[right]]: return False
            left += 1
            right -= 1
        return True
