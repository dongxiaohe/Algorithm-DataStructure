class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        while l2:
            stack2.append(l2)
            l2 = l2.next
        dummy, rem = ListNode(0), 0
        while stack1 or stack2:
            s = (stack1.pop().val if stack1 else 0) + (stack2.pop().val if stack2 else 0) + rem
            tmp, rem = ListNode(s % 10), s // 10
            tmp.next = dummy.next
            dummy.next = tmp
        if rem == 1:
            dummy.val = 1
            return dummy
        return dummy.next
