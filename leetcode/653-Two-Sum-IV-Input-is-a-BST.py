class Solution:
    def findTarget(self, root, k):
        if not root: return False
        stack, state = [root], set()
        while stack:
            tmp = stack.pop()
            if k - tmp.val in state: return True
            state.add(tmp.val)
            if tmp.left: stack.append(tmp.left)
            if tmp.right: stack.append(tmp.right)
        return False
