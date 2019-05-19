class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        n = head.next
        head.next = self.swapPairs(head.next.next)
        n.next = head
        return n

