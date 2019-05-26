class Solution(object):
    def sortedListToBST(self, head):
        def _buildTree(head, tail):
            if head == tail: return None
            slow = fast = head
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next
            root = TreeNode(slow.val)
            root.left = _buildTree(head, slow)
            root.right = _buildTree(slow.next, tail)
            return root
        if not head: return None
        return _buildTree(head, None)
