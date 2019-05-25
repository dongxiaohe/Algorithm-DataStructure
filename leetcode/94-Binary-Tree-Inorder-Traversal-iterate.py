class Solution(object):
    def inorderTraversal(self, root):
        if not root: return []
        stack, result, cur = [], [], root
        while cur or stack:
            while cur: 
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result

