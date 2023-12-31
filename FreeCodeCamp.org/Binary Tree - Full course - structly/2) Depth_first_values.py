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

# Iterative Version 

# def depthFirstValues(root):
#     if root == None: return []
#     result = []
#     stack = [root]
#     while len(stack) > 0:
#         current = stack.pop()
#         # print(current.val)
#         result.append(current.val)

#         if current.right:        
#             stack.append(current.right)
#         if current.left:
#             stack.append(current.left)
#     return result


# Recursive Version

def depthFirstValues(root):
    if root == None: return []
    leftValues = depthFirstValues(root.left)    # b, d, e
    rightValues = depthFirstValues(root.right)  # c, f
    return [root.val] + leftValues + rightValues

print(depthFirstValues(a))