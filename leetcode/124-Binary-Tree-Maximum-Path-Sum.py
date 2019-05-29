class Solution:
    def maxPathSum(self, root):
        def _maxPathSum(root, state):
            if not root: return 0
            left = max(0, _maxPathSum(root.left, state))
            right = max(0, _maxPathSum(root.right, state)
            state["max"] = max(state["max"], left + right + root.val)
            return max(left, right) + root.val
        state = {"max": float("-inf")}
        _maxPathSum(root, state)
        return state["max"]
