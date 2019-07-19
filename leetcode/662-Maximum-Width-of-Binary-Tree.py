class Solution:
    def widthOfBinaryTree(self, root):
        def _dfs(node, level, pos, state):
            if not node: return
            if level not in state["leftmost"]:
                state["leftmost"][level] = pos
            state["width"] = max(state["width"], pos - state["leftmost"][level] + 1)
            _dfs(node.left, level + 1, 2 * pos, state)
            _dfs(node.right, level + 1, 2 * pos + 1, state)
        state = {
            "leftmost": {},
            "width": 0
        }
        _dfs(root, 1, 0, state)
        return state["width"]
