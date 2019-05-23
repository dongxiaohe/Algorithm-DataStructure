class Solution:
    def deleteDuplicates(self, head):
        fakeHead, isDuplicate = ListNode(0), False
        cur = fakeHead
        while head:
            while head.next and head.next.val == head.val:
                head = head.next
                isDuplicate = True
            if not isDuplicate: 
                cur.next = head
                cur = cur.next
            if not head.next: cur.next = None
            head = head.next
            isDuplicate = False
        return fakeHead.next
