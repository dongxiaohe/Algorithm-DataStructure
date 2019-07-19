class Solution:
    def countNodes(self, root):
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 if root else 0
            
