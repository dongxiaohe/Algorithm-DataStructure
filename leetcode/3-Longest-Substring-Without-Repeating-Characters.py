class Solution:
    def lengthOfLongestSubstring(self, s):
        start = maximum = 0 
        count = {}
        for index, str in enumerate(s):
            if str in count:
                start = max(start, count[str] + 1)
            count[str] = index
            maximum = max(maximum, index - start + 1)
        return maximum
             
