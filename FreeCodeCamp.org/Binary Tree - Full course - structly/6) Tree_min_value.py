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

def treeMin(root):
    if root is None: return 0
    queue = [root]
    minimum = None
    while len(queue) > 0:
        current = queue.pop()
        if (minimum == None) or (current.val < minimum) :
            minimum = current.val
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return minimum

# def treeMin(root):
#     if root is None: return 
#     leftMin = treeMin(root.left)
#     rightMin = treeMin(root.right)
#     return min(root.val, leftMin, rightMin)

print(treeMin(a))