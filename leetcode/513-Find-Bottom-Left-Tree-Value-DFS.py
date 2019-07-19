class Solution:
    def findBottomLeftValue(self, root):
        def _bottomLeft(node, level, state):
            if node:
                _bottomLeft(node.left, level + 1, state)
                if level > state["maxLevel"]:
                    state["maxLevel"] = level
                    state["result"] = node.val
                _bottomLeft(node.right, level + 1, state)
        state = {
            "maxLevel": -1,
            "result": None
        }
        _bottomLeft(root, 0, state)
        return state["result"]
