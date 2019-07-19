class Solution(object):
    def isSubtree(self, s, t):
        def isSame(s, t):
            if not s and not t: return True
            if not s or not t or s.val != t.val: return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)
        if isSame(s, t): return True
        if not s and not t: return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
