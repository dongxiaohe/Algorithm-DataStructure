class Solution:
    def zigzagLevelOrder(self, root):
        def _traverse(cur, result, level):
            if not cur: return
            if len(result) <= level: result.append([])
            if level % 2 == 0: result[level].append(cur.val)
            else: result[level].insert(0, cur.val)
            _traverse(cur.left, result, level + 1)
            _traverse(cur.right, result, level + 1)
        result = []
        _traverse(root, result, 0)
        return result

