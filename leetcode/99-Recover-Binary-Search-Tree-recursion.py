class Solution:
    first, second, pre = None, None, TreeNode(float("-inf")) 

    def recoverTree(self, root):
        def _traverse(root): 
            if not root: return
            _traverse(root.left)
            if not self.first and self.pre.val >= root.val: self.first = self.pre
            if self.first and self.pre.val >= root.val: self.second = root
            self.pre = root 
            _traverse(root.right)
        _traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
