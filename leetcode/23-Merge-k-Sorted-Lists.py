class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
    def mergeKLists(self, lists):
        def _mergeTwoLists(list1, list2):
            head = node = ListNode(0)
            while list1 and list2:
                if list1.val <= list2.val:
                    node.next = list1
                    list1 = list1.next
                else: 
                    node.next = list2
                    list2 = list2.next
                node = node.next
            if not list1:
                node.next = list2
            else:
                node.next = list1
            return head.next
        num = len(lists)
        if num == 0:
            return None
        step = 1
        while step < num:
            for i in range(0, num - step, step * 2):
                lists[i] = _mergeTwoLists(lists[i], lists[i + step])
            step *= 2
        return lists[0]
