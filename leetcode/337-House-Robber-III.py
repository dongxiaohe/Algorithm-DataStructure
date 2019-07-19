class Solution(object):
    def rob(self, root):
        def maxNonAdjacent(root):
            result = {
                "incl": 0,
                "excl": 0
            }
            if not root: return result 
            left = maxNonAdjacent(root.left)
            right = maxNonAdjacent(root.right)
            result["incl"] = left["excl"] + right["excl"] + root.val
            result["excl"] = max(left["incl"], left["excl"]) + max(right["incl"], right["excl"])
            return result
        result = maxNonAdjacent(root)
        return max(result["incl"], result["excl"])
