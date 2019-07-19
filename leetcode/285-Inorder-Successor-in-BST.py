class Solution(object):
    def __init__(self):
        self.result = None
    def inorderSuccessor(self, root, p):
        def find(node, _max):
            if node:
                if p.val < node.val <= _max:
                    self.result = node
                    find(node.left, node.val)
                if node.val <= p.val: find(node.right, _max)
                else: find(node.left, _max)
        find(root, float("inf"))
        return self.result
