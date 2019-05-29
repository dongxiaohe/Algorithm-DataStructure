class Solution(object):
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

"""
    1
   / \
  2   5
 / \   \
3   4   6

Basically, the idea to shift tree follows these steps:

    1
   / \
  2   5
 / \   \
3   4   6

    1
     \
      2
     / \
    3   4
         \
          5
           \
            6
            
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

"""
