class Solution:
    def leafSimilar(self, root1, root2):
        def _dfs(node):
            if not node: return 
            if not node.left and not node.right: yield node.val
            for i in _dfs(node.left): yield i
            for i in _dfs(node.right): yield i
        from itertools import zip_longest
        return all(x == y for x, y in zip_longest(_dfs(root1), _dfs(root2)))
