class Solution(object):
    def insert(self, head, insertVal):
        newNode = Node(insertVal, None)
        if not head: return newNode
        node = head
        while True:
            if node.next.val < node.val and (node.next.val >= insertVal or node.val <= insertVal):
                break
            if node.val <= insertVal <= node.next.val:
                break
            if node.next == head:
                break
            node = node.next
        newNode.next = node.next
        node.next = newNode
        return head
