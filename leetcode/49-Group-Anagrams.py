class Solution:
    def groupAnagrams(self, strs):
        result = collections.defaultdict(list)
        for str in strs:
            count = [0] * 26
            for ch in str:
                count[ord(ch) - 97] += 1
            result[tuple(count)].append(str)
        return result.values()
