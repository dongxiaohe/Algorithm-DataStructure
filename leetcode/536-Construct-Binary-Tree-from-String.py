class Solution(object):
    def str2tree(self, S):
        ix = S.find("(")
        if ix == -1: return TreeNode(int(S)) if S else None

        opened = 0
        for jx, ch in enumerate(S):
            if ch == "(": opened += 1
            elif ch == ")": opened -= 1
            if jx > ix and opened == 0: break

        root = TreeNode(int(S[:ix]))
        root.left = self.str2tree(S[ix + 1: jx])
        root.right = self.str2tree(S[jx + 2: -1])
        return root
