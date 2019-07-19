class Solution(object):
    def tree2str(self, t):
        if not t: return ""
        result = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if not left and not right: return result
        if not left: return result + "()({})".format(right)
        if not right: return result + "({})".format(left)
        return result + "({})({})".format(left, right)
