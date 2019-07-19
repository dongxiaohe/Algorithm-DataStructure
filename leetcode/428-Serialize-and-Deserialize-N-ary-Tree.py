class Codec:

    def serialize(self, root):
        result = []
        if root:
            result.append(root.val)
            result.append(len(root.children)) # key point
            for child in root.children:
                result.extend(self.serialize(child))
        return result

    def deserialize(self, data):
        while data:
            val = data.pop(0)
            size = data.pop(0)
            if val == None: return 
            node = Node(val, [])
            for _ in range(size):
                node.children.append(self.deserialize(data))
            return node
        return None
