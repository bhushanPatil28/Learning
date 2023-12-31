class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None
    
node0 = TreeNode(2)
node1 = TreeNode(3)
node3 = TreeNode(1)
node2 = TreeNode(5)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

node0.left = node1
node0.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node4.right = node6
node5.left = node7
node5.right = node8

tree = node5

print(tree.key)
print(tree.left.key)
print(tree.right.key)