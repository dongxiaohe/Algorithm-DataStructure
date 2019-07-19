class Solution:
    def isCompleteTree(self, root):
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                tmp = queue.pop(0)
                if not tmp: return all(map(lambda x: x == None, queue))
                queue.append(tmp.left)
                queue.append(tmp.right)
        return True
