class Solution(object):
    def kthSmallest(self, root, k):
        result = {"count": 0, "val": None}
        def _kthSmallest(root, k, result):
            if root:
               _kthSmallest(root.left, k, result)
               result["count"] += 1
               if result["count"] == k: result["val"] = root.val
               _kthSmallest(root.right, k, result)
            return None
     
        _kthSmallest(root, k, result)
        return result["val"]
