class Solution(object):
    def alienOrder(self, words):
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    pre[b].add(a)
                    suc[a].add(b)
                    break
        chars = set("".join(words))
        free = chars - set(pre)
        result = ""
        while free:
            ch = free.pop()
            result += ch
            for dep in suc[ch]:
                pre[dep].discard(ch)
                if len(pre[dep]) == 0: free.add(dep)
        return result if len(result) == len(chars) else ""

