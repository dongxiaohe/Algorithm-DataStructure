class Solution(object):
    def expressiveWords(self, S, words):
        def group_by(_str):
            return zip(*[(ch, len(list(group))) for ch, group in itertools.groupby(_str)])
        result = 0
        s_ch, s_count = group_by(S)
        for word in words:
            word_ch, word_count = group_by(word)
            if word_ch != s_ch: continue
            if all(a == b or a >= max(b, 3) for a, b in zip(s_count, word_count)): result += 1
        return result
