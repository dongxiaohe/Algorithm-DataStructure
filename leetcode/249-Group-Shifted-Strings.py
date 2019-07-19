class Solution(object):
    def groupStrings(self, strings):
        maskMap = collections.defaultdict(list)
        for _str in strings:
            mask = "0"
            for i in range(1, len(_str)):
                diff = ord(_str[i]) - ord(_str[i - 1])
                if diff < 0: diff += 26
                mask += "&" + str(diff)
            maskMap[mask].append(_str)
        return maskMap.values()
