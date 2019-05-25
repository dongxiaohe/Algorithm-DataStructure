class Solution(object):
    def isValidBST(self, root):
        if not root: return True
        stack, pre = [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # if pre: print(pre.val, root.val)
            """
            Convert binary search tree into list of pair. 
                T
               A B
              C D
              
              C < A , A < D , D < T
            """
            if pre and pre.val >= root.val: return False
            pre, root = root, root.right
        return True

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
two.left = one
two.right = five
three.left = two
three.right = four
four.right = six

print(Solution().isValidBST(three))