class Solution(object):
    def reverseList(self, head):
        newHead = None
        while head:
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode
        return newHead
