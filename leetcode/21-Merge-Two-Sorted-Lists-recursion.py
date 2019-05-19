class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    def mergeTwoLists(self, l1, l2):
        def _mergeTwoLists(l1, l2, node):
            if not l1:
                node.next = l2
                return head
            elif not l2:
                node.next = l1
                return head
            if l1.val <= l2.val: 
                node.next = l1
                _mergeTwoLists(l1.next, l2, node.next)
            else:
                node.next = l2 
                _mergeTwoLists(l1, l2.next, node.next)
        head = ListNode(0)
        node = head
        _mergeTwoLists(l1, l2, node)
        return head.next
