class Solution(object):
    def removeElements(self, head, val):
        cur = ListNode(0)
        cur.next = head
        dummy_head = cur
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else: cur = cur.next
        return dummy_head.next

