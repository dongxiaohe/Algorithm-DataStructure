class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        result, queue = [], [root]
        while queue:
            size = len(queue)
            tmpList = []
            for i in range(size):
                node = queue.pop(0)
                tmpList.append(node.val)
                queue.extend(node.children)
            result.append(tmpList)
        return result
