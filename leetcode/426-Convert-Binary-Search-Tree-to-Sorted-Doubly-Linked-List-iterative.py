class Solution(object):
    def treeToDoublyList(self, root):
        if not root: return None
        first, last, stack, node = None, None, [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if not first:
                first = last = node
            else:
                last.right = node
                node.left = last
                last = last.right
            node = node.right
        first.left = last
        last.right = first
        return first

