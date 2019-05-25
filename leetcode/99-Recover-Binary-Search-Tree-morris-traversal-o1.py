class Solution:
    def recoverTree(self, root):
        curr, tmp, prev, swap1, swap2 = root, None, None, None, None
        while curr:
            if curr.left is None:
                if prev and prev.val > curr.val:
                    # print(prev.val, curr.val)
                    """

                        if we don't use prev and just use tmp, we can print(curr.val) to see an in order list. prev is a trick on top of morris traversal to record each curr previous value.
                    """
                    if not swap1: swap1 = prev
                    swap2 = curr
                prev = curr
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right is not None and tmp.right is not curr:
                    tmp = tmp.right
                if tmp.right is curr:
                    if prev and prev.val > curr.val:
                        # print(prev.val, curr.val)
                        if not swap1: swap1 = prev
                        swap2 = curr
                    prev = curr
                    tmp.right = None
                    curr = curr.right
                else:
                    tmp.right = curr
                    curr = curr.left
        swap1.val, swap2.val = swap2.val, swap1.val

