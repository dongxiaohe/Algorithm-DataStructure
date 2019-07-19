class Solution(object):
    def sumOfLeftLeaves(self, root):
        result = 0
        if root:
            if root.left and not root.left.left and not root.left.right:
                result += root.left.val 
            result += self.sumOfLeftLeaves(root.left)
            result += self.sumOfLeftLeaves(root.right)
        return result  
