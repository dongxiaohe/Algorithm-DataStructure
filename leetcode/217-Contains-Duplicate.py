class Solution(object):
    def containsDuplicate(self, nums):
        kv = collections.defaultdict(bool)
        for i in nums:
            if i in kv: return True
            kv[i] = True
        return False
