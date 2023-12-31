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


# # breadth_first_value solutio
# def treeIncludes(root, target):
#     if root is None: 
#         return False
#     queue = [root]
#     while len(queue) > 0:
#         current = queue.pop(0)
#         if current.val == target:
#             return True
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)
#     return False

# Depth_first - recursive
def treeIncludes(root, target):
    if root is None: return False
    if root.val == target:
        return True
    return treeIncludes(root.left, target) or treeIncludes(root.right, target)

print(treeIncludes(a, 'e'))