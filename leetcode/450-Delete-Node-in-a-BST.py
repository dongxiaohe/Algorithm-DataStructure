class Solution(object):
    def deleteNode(self, root, key):
        def findMinAndRemove(current, parent):
            if not current.left:
                parent.right = current.right
                return current.val
            while current.left:
                parent = current
                current = current.left
            parent.left = current.right
            return current.val
        if not root: return None
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.right:
                    return root.left
                elif not root.left:
                    return root.right
                else:
                    root.val = findMinAndRemove(root.right, root)
            return root

