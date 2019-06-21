arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class SegmentTree:
    def __init__(self, val, start, end, left = None, right = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

def buildTree(i, j, arr):
    if i == j:
        return SegmentTree(arr[i], i, j)
    mid = i + ((j - i) >> 1)
    left = buildTree(i, mid , arr)
    right = buildTree(mid + 1, j, arr)
    return SegmentTree(left.val + right.val, i, j, left, right)

def updateTree(root, index, val):
    if root.start == root.end == index:
        root.val = val
        return
    mid = root.start + ((root.end - root.start) >> 1)
    if index <= mid:
        updateTree(root.left, index, val)
    else:
        updateTree(root.right, index, val)
    root.val = root.left.val + root.right.val

def queryTree(root, i, j):
    if i == root.start and j == root.end: return root.val
    mid = root.start + ((root.end - root.start) >> 1)
    if j <= mid:
        return queryTree(root.left, i, j)
    elif i >= mid:
        return queryTree(root.right, i, j)
    else:
        return queryTree(root.left, i, mid) + queryTree(root.right, mid + 1, j)

root = buildTree(0, len(arr) - 1, arr)
print(root.val, root.start, root.end)
left = root.left
print(left.val, left.start, left.end)
right = root.right
print(right.val, right.start, right.end)

def printNode(node):
    if node and not node.left and not node.right: print(node.val, node.start, node.end)
    if node.left: printNode(node.left)
    if node.right: printNode(node.right)

updateTree(root, 6, 15)
print(root.val)
updateTree(root, 6, 7)
print(root.val)

print(queryTree(root, 0, 9))
print(queryTree(root, 3, 9))
print(queryTree(root, 3, 4))
print(queryTree(root, 3, 6))

for i in range(len(arr)):
    print(queryTree(root, i, i))
