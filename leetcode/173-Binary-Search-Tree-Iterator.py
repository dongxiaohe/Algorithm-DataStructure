class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        tmpNode = node.right
        while tmpNode:
            self.stack.append(tmpNode)
            tmpNode = tmpNode.left
        return node.val
