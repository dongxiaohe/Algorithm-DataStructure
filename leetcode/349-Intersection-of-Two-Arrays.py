class Solution(object):
    def intersection(self, nums1, nums2):
        numsSet = set(nums1)
        result = set()
        for each in nums2:
            if each in numsSet: result.add(each)
        return list(result)
