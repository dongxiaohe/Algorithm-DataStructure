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
