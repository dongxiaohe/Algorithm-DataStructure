class Solution:
    def reverseKGroup(self, head, k):
        if k <= 1 or not head: return head
        preHeader = ListNode(-1)
        preHeader.next = head
        cur, pre, num = preHeader.next, preHeader, 0
        while cur:
            num += 1
            cur = cur.next
        while num >= k:
            cur = pre.next
            nex = cur.next
            for i in range(k - 1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next
            pre = cur
            num -= k
        return preHeader.next

