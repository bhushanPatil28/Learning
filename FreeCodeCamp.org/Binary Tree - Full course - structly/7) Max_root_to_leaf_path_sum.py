import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(15)
f = Node(12)
#        5
#       / \
#      11   3
#     / \   \
#    4   15   12
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def maxPathSum(root):
    if root is None: return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    maxChildPathSum = max(maxPathSum(root.left), maxPathSum(root.right))
    return root.val + maxChildPathSum

print(maxPathSum(a))
