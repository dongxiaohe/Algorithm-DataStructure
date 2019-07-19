class Solution(object):
    def kthSmallest(self, root, k):
        stack, count = [], 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            count += 1 
            if count == k: return root.val
            root = root.right
        return None

