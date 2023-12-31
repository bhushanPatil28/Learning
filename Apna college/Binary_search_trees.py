class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]

values = [5,1,3,4,2,7]

def buildTree(values):
    if values is None:
        return 0 
    root = Node(values[0])
    values.pop(0)
    if root.value > values[0]:
        return root.left = buildTree(values)
    else:
        return root.right = buildTree(values)
    return root

def build(root, values):
    if root is None:
        root = Node(values)
        return root 
    if root.value > values:
        root.left = build(root.left, values)
    else:
        root.right = build(root.right, values)
    return root

for i in values:
    root = build(root, values[i])



def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)

    # if the node is empty
    if node is None:
        print(space*level + '@')
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.value))
        return 
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.value))
    display_keys(node.left, space, level+1)

display_keys(root)
