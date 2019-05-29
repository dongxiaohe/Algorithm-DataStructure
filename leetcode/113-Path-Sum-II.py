class Solution(object):
    def pathSum(self, root, sum):
        def _pathSum(root, sum, result, acc):
            if not root: return
            if root.val == sum and not root.left and not root.right:
                result.append(acc + [root.val])
                return
            _pathSum(root.left, sum - root.val, result, acc + [root.val])
            _pathSum(root.right, sum - root.val, result, acc + [root.val])
        result = []
        _pathSum(root, sum, result, [])
        return result

