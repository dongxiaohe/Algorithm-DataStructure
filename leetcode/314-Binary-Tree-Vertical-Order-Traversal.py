class Solution(object):
    def verticalOrder(self, root):
        if not root: return []
        level = [(root, 0)]
        colsMap = collections.defaultdict(list)
        while level:
            newLevel = []
            for node, colIndex in level:
                colsMap[colIndex].append(node.val)
                if node.left: newLevel.append((node.left, colIndex - 1))
                if node.right: newLevel.append((node.right, colIndex + 1))
            level = newLevel
        result = [0] * len(colsMap)
        offset = -min(colsMap.keys())
        for k, v in colsMap.items():
            result[k + offset] = v
        return result
