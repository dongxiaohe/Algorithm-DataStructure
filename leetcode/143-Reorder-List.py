class Solution:
    def reorderList(self, head):
        if not head or not head.next: return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        first, second = slow, slow.next
        while second.next: # 1->2->3->4->5->6 to 1->2->3->6->5->4
            third = second.next
            second.next = third.next
            third.next = first.next
            first.next = third
        first, second, third = head, slow, slow.next
        while first != second: # 1->2->3->6->5->4 to 1->6->2->5->3->4
            second.next = third.next
            first_1 = first.next
            first.next = third
            third.next = first_1
            first = first_1
            third = second.next
