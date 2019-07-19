class Solution:
    def isUnivalTree(self, root):
        uniValue, queue = None, [root]
        while queue: 
            node = queue.pop(0)    
            if uniValue == None: uniValue = node.val
            elif uniValue != node.val: return False
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return True
