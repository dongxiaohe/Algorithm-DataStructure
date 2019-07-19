class Solution(object):
    def preorder(self, root):
        if not root: return []
        stack, output = [root], []
        while stack:
            tmp = stack.pop()
            output.append(tmp.val)
            stack.extend(tmp.children[::-1])
        return output
