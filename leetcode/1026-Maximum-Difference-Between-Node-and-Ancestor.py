class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node, low, high):
            if not node: return high - low
            else:
                high = max(high, node.val)
                low = min(low, node.val)
                return max(dfs(node.left, low, high), dfs(node.right, low, high))
        return dfs(root, root.val, root.val) if root else 0
