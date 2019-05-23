class Solution:
    def rotateRight(self, head, k):
        length, tail = 1, head
        if not head: return head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head
        k = length - k % length
        while k:
            tail = tail.next
            k -= 1
        newH = tail.next
        tail.next = None
        return newH
