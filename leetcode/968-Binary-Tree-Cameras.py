class Solution:
    def minCameraCover(self, root):
        self.res = 0
        def dfs(node): 
            if not node: return 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.res += 1
                return 1
            else: return 2 if left == 1 or right == 1 else 0

        return (dfs(root) == 0) + self.res
