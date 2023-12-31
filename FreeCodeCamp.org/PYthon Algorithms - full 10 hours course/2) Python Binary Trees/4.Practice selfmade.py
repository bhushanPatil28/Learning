class TreeNodes:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNodes(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None 
    else:
        node = TreeNodes(data)
    return node



tree_tuple = ((None, 40, (42, 45, 49)), 50, (55, 60, 95))


tree2 = parse_tuple(tree_tuple)
# print(tree2.key)
# print(tree2.left.key, tree2.right.key)
# print(tree2.left.left,tree2.left.right.key, tree2.right.left.key, tree2.right.right.key)
# print(tree2.left.right.left.key, tree2.left.right.right.key)


def display_keys(node, space = '\t', level=0):
    if node is None:
        print(level*space + '@')
        return
    if node.left is None and node.right is None:
        print(level*space + str(node.key))
        return 
    display_keys(node.right, space, level+1)
    print(level*space + str(node.key))
    display_keys(node.left, space, level+1)

display_keys(tree2, ' ')