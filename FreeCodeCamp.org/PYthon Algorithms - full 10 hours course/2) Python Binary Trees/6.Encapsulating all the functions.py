class TreeNode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(self.left.height() if self.left else 0, self.right.height() if self.right else 0)

    def size(self):
        if self is None:
            return 0 
        return 1 + (self.left.size() if self.left else 0) + (self.right.size() if self.right else 0)
    
    def traverse_in_order(self):
        if self is None:
            return []
        return (self.left.traverse_in_order() if self.left else []) + [self.key] + (self.right.traverse_in_order() if self.right else [])
    
    def display_keys(self, space='\t', level=0):
        if self is None:
            print(space*level + '@')
            return
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return
        if self.right:
            self.right.display_keys(space, level + 1)
        print(space*level + str(self.key))
        if self.left:
            self.left.display_keys(space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key 
        return (self.left.to_tuple() if self.left else None), self.key, (self.right.to_tuple() if self.right else None)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None 
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

tree = TreeNode.parse_tuple(tree_tuple)

tree.display_keys(' ')

print(tree.height())
print(tree.size())
print(tree.traverse_in_order())
print(tree.to_tuple())
