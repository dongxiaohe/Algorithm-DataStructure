class Solution:
    def isSubsequence(self, s, t):
        def binarySearch(indexList, pre):
            low, high = 0, len(indexList) - 1
            while low <= high:
                mid = (low + high) >> 1
                if indexList[mid] < pre: low = mid + 1
                else: high = mid - 1
            return indexList[low] if low != len(indexList) else -1

        kv = collections.defaultdict(list)
        for i in range(len(t)):
            kv[t[i]].append(i)
        pre = 0
        for ch in s:
            if not kv[ch]: return False
            pre = binarySearch(kv[ch], pre)
            if pre == -1: return False
            pre += 1
        return True
            

