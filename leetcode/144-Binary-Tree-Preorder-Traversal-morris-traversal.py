class Solution:
    def preorderTraversal(self, root):
        current, result = root, []
        while current:
            if not current.left:
                result.append(current.val)
                current = current.right
            else:
                pre = current.left 
                while pre.right and pre.right is not current: pre = pre.right
                if not pre.right:
                    result.append(current.val)
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    current = current.right
        return result

