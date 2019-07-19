class Solution:
    def countUnivalTrees(self, root):
        def helper(node):
            if not node: return 0, True
            left_count, is_left_unival = helper(node.left)
            right_count, is_right_unival = helper(node.right)
            total = left_count + right_count
            if is_left_unival and is_right_unival:
                if node.left and node.left.val != node.val:
                    return total, False
                if node.right and node.right.val != node.val:
                    return total, False
                return 1 + total, True
            return total, False
        count, _ = helper(root)
        return count
