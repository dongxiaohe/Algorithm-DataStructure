class Codec:

    def serialize(self, root):
        def _serialize(node, result): 
            if not node:
                result.append(None)
                return
            else:
                result.append(node.val)
                _serialize(node.left, result)
                _serialize(node.right, result)
        result = []
        _serialize(root, result)
        return result

    def deserialize(self, data):
        if data:
            tmpVal = data.pop(0)
            if tmpVal == None: return None
            node = TreeNode(tmpVal)
            node.left = self.deserialize(data)
            node.right = self.deserialize(data)
            return node
