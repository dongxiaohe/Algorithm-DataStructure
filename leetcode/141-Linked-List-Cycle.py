class Solution(object):
    def hasCycle(self, head):
        if not head: return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False