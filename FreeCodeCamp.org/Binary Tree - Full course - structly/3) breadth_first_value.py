class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
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

def breadthFirstValue(root):
    if root is None:
        return []
    
    queue = [root]
    result = []

    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.val)
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
            queue.append(current.right)

    return result
    

print(breadthFirstValue(a))