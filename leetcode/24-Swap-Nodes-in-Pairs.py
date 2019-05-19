class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    def swapPairs(self, head):
        result = head.next if head and head.next else head
        anchor = None 
        while head and head.next:
            tmp = head.next
            if anchor:
                anchor.next = tmp
            head.next = tmp.next
            tmp.next = head
            anchor = head
            head = head.next
        return result


