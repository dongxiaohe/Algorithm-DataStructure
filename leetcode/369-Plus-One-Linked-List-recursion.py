class Solution(object):
    def plusOne(self, head):
        def _plus_one(node):
            if not node: return 1
            carry = _plus_one(node.next)
            tmp_val = node.val + carry
            node.val = tmp_val % 10
            return tmp_val // 10
        if _plus_one(head) == 1:
            dummyHead = ListNode(1)
            dummyHead.next = head
            return dummyHead
        return head
