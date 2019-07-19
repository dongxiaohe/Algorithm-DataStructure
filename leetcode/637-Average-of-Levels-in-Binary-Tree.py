class Solution:
    def averageOfLevels(self, root):
        row, result = [root], []
        while row:
            tmpRow = []
            result.append(sum(map(lambda x: x.val, row)) / len(row))
            for node in row:
                for kid in (node.left, node.right):
                    if kid: tmpRow.append(kid)
            row = tmpRow
        return result
