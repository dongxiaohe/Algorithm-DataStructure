class Solution:
    def addOneRow(self, root, v, d):
        dummy, dummy.left = TreeNode(v), root
        row = [dummy]
        """
        BFS in python, it can be simplified as:
        row = [kid for node in row for kid in (node.left, node.right) if kid]
        """
        for _ in range(d - 1):
            tmpRow = []
            for node in row:
                for kid in (node.left, node.right):
                    if kid: tmpRow.append(kid)
            row = tmpRow 
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left
            
