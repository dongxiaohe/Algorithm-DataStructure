class Solution(object):
    def detectCycle(self, head):
        slow, fast, cycle = head, head, False
        while slow and fast:
            slow = slow.next
            if not fast.next: return None
            fast = fast.next.next
            if slow == fast: 
                cycle = True
                break
        if not cycle: return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
