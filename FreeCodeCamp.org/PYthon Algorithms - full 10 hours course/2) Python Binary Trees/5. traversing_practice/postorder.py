class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


tree_node = ((('a','b',None),'c',('d', 'e', 'f')),'g',('h','i',(None, 'j', 'k')))
def parse_tuple(data):
    if data is None:
        node = None 
    elif isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    else:
        node = TreeNode(data)
    return node

def display_tree(node, space = '\t', level=0):
    if node is None:
        print(level*space + '@')
        return
    if node.left is None and node.right is None:
        print(level*space + str(node.key))
        return
    display_tree(node.right, space, level+1)
    print(space*level + str(node.key))
    display_tree(node.left, space, level+1)


def postOrderPrint(node):
    if node is None:
        return 
    else:
        print(node.key, end = ' ')
        postOrderPrint(node.right)
        postOrderPrint(node.left)

tree = parse_tuple(tree_node)
postOrderPrint(tree)