class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        head = result
        addOne = 0
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val 
                l1 = l1.next
            if l2:
                total += l2.val 
                l2 = l2.next
            total += addOne
            result.next = ListNode(total % 10)
            result = result.next
            addOne = int(total >= 10)
        if addOne == 1:
            result.next = ListNode(1)
        return head.next
