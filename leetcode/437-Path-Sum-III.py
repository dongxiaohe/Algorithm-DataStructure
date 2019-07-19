class Solution(object):
    def pathSum(self, root, sum):
        def _pathSumFrom(root, sum):
            if root == None: return 0
            acc = 1 if root.val == sum else 0 
            return acc + _pathSumFrom(root.left, sum - root.val) + _pathSumFrom(root.right, sum - root.val)
        if root == None: return 0
        return _pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
