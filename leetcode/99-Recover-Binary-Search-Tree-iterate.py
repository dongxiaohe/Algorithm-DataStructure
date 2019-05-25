class Solution:
    def recoverTree(self, root):
        stack, swap, pre = [], [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val:
                swap.extend([pre, root])
            pre = root
            root = root.right
        swap[0].val, swap[-1].val = swap[-1].val, swap[0].val
