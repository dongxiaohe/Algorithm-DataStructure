class Solution:
    def convertBST(self, root):
        def _convert(node, sum, state):
            if not node: return
            if node.right: _convert(node.right, sum, state)
            node.val += state["sum"]
            sum = node.val
            state["sum"] = node.val
            if node.left: _convert(node.left, sum, state)
        """
        Be aware of using what data type recursive function
        If it is a primitive type, the value is early evaluated.
        Thus, we have to use object lazily reference the sum value
        
        """
        _convert(root, 0, {"sum": 0})
        return root
