class Solution:
    def connect(self, root):
        dummyHead = TreeLinkNode(0)
        p = dummyHead
        while root:
            if root.left:
                p.next = root.left
                p = p.next
            if root.right:
                p.next = root.right
                p = p.next
            if root.next:
                root = root.next
            else:
                root = dummyHead.next
                dummyHead.next = None
                p = dummyHead
"""
The trick of this problem is to use dummyHead to point to the head of next level. and use P to point to the current one of next level.
"""