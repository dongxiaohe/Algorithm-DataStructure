"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

Leetcode problem 297 https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Using pre-order traversal to serialize the tree makes sense, coz it is very straightforward to deserialize the identical tree. Other dfs approach like in-order and post-order seems difficult to do it. BFS can do it, but it would use more spaces.
"""
class Codec:
    def serialize(self, root):
        def _serialize(root, result):
            if not root: result.append(None)
            else:
                result.append(root.val)
                _serialize(root.left, result)
                _serialize(root.right, result)
        result = []
        _serialize(root, result)
        return result

    def deserialize(self, data):
        if data:
            val = data.pop(0)
            if val == None: return None
            node = TreeNode(val)
            node.left = self.deserialize(data)
            node.right = self.deserialize(data)
            return node
