class Solution(object):
    def findAnagrams(self, s, p):
        def delete_if_zero(dictionary, ch):
            if dictionary[ch] == 0:
                del dictionary[ch]

        freq = collections.defaultdict(int)
        for ch in p:
            freq[ch] += 1
        for ch in s[:len(p)]:
            freq[ch] -= 1
            delete_if_zero(freq, ch)
        result = []
        if not freq:
            result.append(0)
        for i in range(len(p), len(s)):
            start_ch, end_ch = s[i - len(p)], s[i]
            freq[start_ch] += 1
            delete_if_zero(freq, start_ch)
            freq[end_ch] -= 1
            delete_if_zero(freq, end_ch)
            if not freq:
                result.append(i - len(p) + 1)
        return result

