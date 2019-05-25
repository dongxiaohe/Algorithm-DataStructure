class Solution:
    def reverseBetween(self, head, m, n):
        if m == n: return head
        start = dummyHead = ListNode(0)
        start.next = head
        for i in range(m - 1):
            start = start.next
        first, second = start.next, start.next.next
        for i in range(n - m):
            first.next = second.next
            second.next = start.next
            start.next = second
            second = first.next
        return dummyHead.next

