class Solution:
    def largestValues(self, root):
        if not root: return []
        queue, result = [root], []
        while queue:
            maxItem = float("-inf")
            i, size = 0, len(queue)
            while i < size:    
                item = queue.pop(0)
                if item.val > maxItem: maxItem = item.val
                if item.left: queue.append(item.left)
                if item.right: queue.append(item.right)
                i += 1
            result.append(maxItem)
        return result
            
