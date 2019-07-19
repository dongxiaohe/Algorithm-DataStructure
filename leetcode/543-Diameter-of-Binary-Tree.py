class Solution:
    def diameterOfBinaryTree(self, root):
        def _depth(node, state):
            if not node: return 0
            left, right = _depth(node.left, state), _depth(node.right, state)
            state["max"] = max(state["max"], left + right)
            return 1 + max(left, right)
        state = {
            "max": 0
        }
        _depth(root, state)
        return state["max"]

