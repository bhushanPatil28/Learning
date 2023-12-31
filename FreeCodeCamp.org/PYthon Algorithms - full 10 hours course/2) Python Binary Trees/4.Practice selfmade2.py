class TreeNode:
    def __init__(self, node):
        self.key = node
        self.left = None
        self.right = None

def parse_tuple(data):
    if isinstance(data, tuple) and len(data)==3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
        return node 
    elif data is None:
        node = None 
    else:
        node = TreeNode(data)
    return node

tree_tuple = ((((50, 100, 120), 125, None), 250, (200, 350, None)), 500, ((550, 625, 700),750, 1000))

tree2 = parse_tuple(tree_tuple)

def display_tree(node, space = '\t', level = 0):
    if node is None:
        print(level*space + '@')
        return
    if node.left is None and node.right is None:
        print(level*space + str(node.key))
        return
    display_tree(node.right, space, level+1)
    print(level*space + str(node.key))
    display_tree(node.left, space, level+1)

display_tree(tree2)
