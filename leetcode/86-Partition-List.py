class Solution:
    def partition(self, head, x):
        s, l = ListNode(0), ListNode(0)
        p1, p2 = s, l
        while head:
            if head.val < x: 
                p1.next = head
                p1 = p1.next 
            else: 
                p2.next = head
                p2 = p2.next 
            head = head.next
        p2.next = None
        p1.next = l.next
        return s.next
