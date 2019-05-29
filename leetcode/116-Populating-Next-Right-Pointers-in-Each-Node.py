class Solution:
    def connect(self, root):
        if not root: return
        queue, squareNum, counter, prev = [root], 0, 0, None
        while queue:
            node = queue.pop(0)
            counter += 1
            node.next = prev
            if counter == 2 ** squareNum: 
                prev = None
                squareNum += 1
                counter = 0
            else: prev = node
            if node.right: queue.append(node.right) 
            if node.left: queue.append(node.left)

"""
1. It should use post order traversal.
2. Use counter and squareNum to record what is the level of tree
3. Don't forget to reset the counter
"""

class TreeLinkNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
        self.next = None

six = TreeLinkNode("6")
five = TreeLinkNode("5")
four = TreeLinkNode("4")
three = TreeLinkNode("3", six)
two = TreeLinkNode("2", four, five)
one = TreeLinkNode("1", two, three)

Solution().connect(one)

print(two.next.val)
print(four.next.val)
print(five.next.val)
print(six.next)
