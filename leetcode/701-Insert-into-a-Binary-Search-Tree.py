class Solution:
    def insertIntoBST(self, root, val):
        cur, node = root, TreeNode(val)
        while True:
            if cur.val <= val:
                if not cur.right:
                    cur.right = node
                    break
                else: cur = cur.right
            else:
                if not cur.left:
                    cur.left = node
                    break
                else: cur = cur.left
        return root
