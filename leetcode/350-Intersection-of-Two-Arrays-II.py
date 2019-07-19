class Solution(object):
    def intersect(self, nums1, nums2):
        map1, result = collections.defaultdict(int), []
        for each in nums1: map1[each] += 1
        for each in nums2: 
            if map1[each]:
                result.append(each)
                map1[each] -= 1 
        return result

