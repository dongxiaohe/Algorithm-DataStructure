class Solution(object):
    def findMode(self, root):
        def morrisTraversal(node, state):
            while node:
                if not node.left:
                    handleValue(state, node)
                    node = node.right
                else:
                    pre = node.left
                    while pre.right and pre.right != node:
                        pre = pre.right
                    if not pre.right:
                        pre.right = node
                        node = node.left
                    else:
                        handleValue(state, node)
                        pre.right = None
                        node = node.right
        def handleValue(state, node):
            if state["pre"] == node.val: state["count"] += 1
            else: state["count"] = 1
            if state["count"] > state["maxCount"]:
                state["result"].clear()
                state["maxCount"] = state["count"]
                state["result"].append(node.val)
            elif state["count"] == state["maxCount"]:
                state["result"].append(node.val)
            state["pre"] = node.val
        state = {
            "result": [],
            "count": 0,
            "maxCount": 0,
            "pre": None
        }
        morrisTraversal(root, state)
        return state["result"]

