class Solution(object):
    def findMode(self, root):
        def _inorderTraverse(root, state):
            if root:
                _inorderTraverse(root.left, state)
                if root.val == state["pre"]:
                    state["count"] += 1
                else:
                    state["count"] = 1
                if state["count"] > state["maxCount"]:
                    state["result"].clear()
                    state["result"].append(root.val)
                    state["maxCount"] = state["count"]
                elif state["count"] == state["maxCount"]:
                    state["result"].append(root.val)
                state["pre"] = root.val
                _inorderTraverse(root.right, state)
        state = {
            "result": [],
            "count": 0,
            "maxCount": 0,
            "pre": None
        }
        _inorderTraverse(root, state)
        return state["result"]

