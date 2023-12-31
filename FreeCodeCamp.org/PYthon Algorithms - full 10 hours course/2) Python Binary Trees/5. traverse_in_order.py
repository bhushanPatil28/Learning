class TreeNode:
    def __init__(self, node):
        self.key = node
        self.left = None
        self.right = None 
 
def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
        return node
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5,(6, 7, 8)))
tree = parse_tuple(tree_tuple)

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

display_tree(tree)

# Treversing each key

def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) + 
           [node.key] +
           traverse_in_order(node.right))

print(traverse_in_order(tree))

# practice these
# binary tree inorder traversal
# binary tree preorder traversal
# binary tree postorder traversal 



# Height and size of a Binary Tree

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree))

def tree_size(node):
    if node is None: 
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

print(tree_size(tree))

# practice these
# maximum-depth-of-binary-tree
# minimum-depth-of-binary-tree
# diameter of binary tree