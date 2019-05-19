from fixture import *

def inOrderRec(node):
    result = []
    if node:
        result = inOrderRec(node.left)
        result.append(node.val)
        result.extend(inOrderRec(node.right))
    return result

def inOrderIter(node):
    stack, result = [], []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result

print("In-order traversal:", inOrderRec(root))
print("In-order traversal:", inOrderIter(root))

def preOrderRec(node):
    result = []
    if node:
        result.append(node.val)
        result.extend(preOrderRec(node.left))
        result.extend(preOrderRec(node.right))
    return result

def preOrderIter(node):
    stack, result = [node], []
    while stack:
        tmp = stack.pop()
        result.append(tmp.val)
        if tmp.right: stack.append(tmp.right)
        if tmp.left: stack.append(tmp.left)
    return result

print("Pre-order traversal:", preOrderRec(root))
print("Pre-order traversal:", preOrderIter(root))

def postOrderRec(node):
    result = []
    if node:
        result.extend(postOrderRec(node.left))
        result.extend(postOrderRec(node.right))
        result.append(node.val)
    return result

def postOrderIter(node):
    stack, result = [node], []
    while stack:
        tmp = stack.pop()
        result.append(tmp.val)
        if tmp.left: stack.append(tmp.left)
        if tmp.right: stack.append(tmp.right)
    return result[::-1]


print("post-order traversal:", postOrderRec(root))
print("post-order traversal:", postOrderIter(root))