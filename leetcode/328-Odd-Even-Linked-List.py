class Solution:
    def oddEvenList(self, head):
        dummyHead1 = odd = ListNode(0)
        dummyHead2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummyHead2.next
        return dummyHead1.next

