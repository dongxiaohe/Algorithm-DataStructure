class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        node = head
        while l1 or l2:
            if not l1:
                node.next = l2
                break
            elif not l2:
                node.next = l1
                break
            if l1.val <= l2.val: 
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        return head.next
