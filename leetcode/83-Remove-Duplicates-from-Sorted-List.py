class Solution:
    def deleteDuplicates(self, head):
        fakeHead = ListNode(0)
        result = fakeHead 
        while head:
            result.next = head
            while head.next and head.val == head.next.val:
                head = head.next
            result.next = head
            result = result.next
            head = head.next
        return fakeHead.next

