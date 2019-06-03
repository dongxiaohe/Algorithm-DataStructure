class Solution(object):
    def copyRandomList(self, head):
        if not head: return None
        curr = head
        while curr:
            headCopy = Node(curr.val, None, None)
            headCopy.next = curr.next
            curr.next = headCopy
            curr = headCopy.next
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        curr = head
        currNew = head.next
        result = currNew
        while curr:
            curr.next = curr.next.next
            currNew.next = currNew.next.next if currNew.next else None
            curr = curr.next
            currNew = currNew.next
        return result

