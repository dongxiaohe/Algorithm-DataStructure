class Solution(object):
    def plusOne(self, head):
        dummy_head = ListNode(0)
        dummy_head.next = head
        i = j = dummy_head
        while j:
            if j.val < 9: i = j
            j = j.next
        i.val += 1
        while i.next:
            i.next.val = 0
            i = i.next
        if dummy_head.val == 0: return dummy_head.next
        return dummy_head

