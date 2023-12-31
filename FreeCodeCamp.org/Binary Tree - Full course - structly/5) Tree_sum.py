class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(1)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)
#        a
#       / \
#      b   c
#     / \   \
#    d   e   f
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# def treeSum(root):
#     if root is None: return 0
#     return root.val + treeSum(root.right) + treeSum(root.left)

def treeSum(root):
    if root is None: return 0
    queue = [ root ]
    sum = 0
    while len(queue) > 0:
        current = queue.pop(0)
        sum += current.val
    
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return sum

print(treeSum(a))