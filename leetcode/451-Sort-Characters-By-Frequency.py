class Solution(object):
    def frequencySort(self, s):
        kv = collections.defaultdict(int)
        for ch in s: kv[ch] += 1
        bucket = collections.defaultdict(list)
        for k in kv: bucket[kv[k]].append(k)
        result = ""
        for i in range(len(s), -1, -1):
            if i in bucket:
                for ch in bucket[i]:
                    result += ch * i
        return result
