class Solution:
    def sortedArrayToBST(self, nums):
        def _buildTree(nums, left, right):
            if left > right: return None
            mid = left + right >> 1
            root = TreeNode(nums[mid])
            root.left = _buildTree(nums, left, mid - 1)
            root.right = _buildTree(nums, mid + 1, right)
            return root
        n = len(nums) - 1
        return _buildTree(nums, 0, n)
