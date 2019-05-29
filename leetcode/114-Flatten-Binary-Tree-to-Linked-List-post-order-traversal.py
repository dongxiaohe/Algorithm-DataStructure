class Solution(object):
    prev = None
    def flatten(self, root):
        if not root: return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

"""
    1
   / \
  2   5
 / \   \
3   4   6

The idea is post order traversal.
 
1st step: 6 -> 5 -> 4 -> 3 -> 2 -> 1
2nd step: we can record prev node to let current node right = prev
3rd step: clean the left to be None

So why we can't use pre-order traversal directly ?
Well, if it is pre-order traversal, the result is (root, left, right). There is a conflict if we want to clean the left and use the left.

"""