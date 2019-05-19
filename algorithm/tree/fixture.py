class TreeNode():
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

leftLeftLeft = TreeNode("left-left-left")
leftLeftRight = TreeNode("left-left-right")
leftRightRight = TreeNode("left-right-right")
rightRightLeft = TreeNode("right-right-left")
leftLeft = TreeNode("left-left", leftLeftLeft, leftLeftRight)
leftRight = TreeNode("left-right", None, leftRightRight)
rightLeft = TreeNode("right-left")
rightRight = TreeNode("right-right", rightRightLeft)
left = TreeNode("left", leftLeft, leftRight)
right = TreeNode("right", rightLeft, rightRight)
root = TreeNode("root", left, right)

"""
           
                                                                  root
                                                    
                                      left                                                    right
                                                                      
                   left-left                      left-right                       right-left       right-right

     left-left-left        right-right-right                left-right-right                                     right-right-right
"""