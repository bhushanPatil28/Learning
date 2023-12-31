class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]
# ----------------------------------------------------------
idx = -1
def TreePreorder(lst):
    global idx  # Declare idx as a global variable
    idx += 1
    if lst[idx] == -1:
        return None
    new_node = Node(lst[idx])
    new_node.left = TreePreorder(lst)
    new_node.right = TreePreorder(lst)
    return new_node  # Return the created node
root = TreePreorder(nodes)
# print(root.value, root.left.value)


# TRAVERSALS


# ----------------------------------------------------------
def preTraversal(root):
    if root == None:
        # print(-1)
        return 
    print(root.value)
    preTraversal(root.left)
    preTraversal(root.right)

# preTraversal(root)
# ----------------------------------------------------------
def inOrderTraverse(root):
    if root == None:
        return
    inOrderTraverse(root.left)
    print(root.value)
    inOrderTraverse(root.right)
    
# inOrderTraverse(root)

# ----------------------------------------------------------
# PostOrder Traversal
def postOrder(root):
    if root == None:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.value, end=" ")
# postOrder(root)


# ----------------------------------------------------------

# Level order traversal

def levelOrder(root):
    if root == None:
        return
    q = []
    q.append(root)
    q.append(None)
    while len(q) > 0:
        current = q.pop(0)
        if current == None:
            print()
            if len(q) == 0:
                break
            else:
                q.append(None)
        else:
            print(current.value, end=" ")
            if current.left != None:
                q.append(current.left)
            if current.right != None:
                q.append(current.right)

# levelOrder(root)

# ---------------------------------------------------------------------
#count of Nodes
def count(root):
    if root is None:
        return 0 
    left = count(root.left)
    right = count(root.right)

    return left + right + 1

# print(count(root))
# ---------------------------------------------------------------------
# Sum of nodes

def sum(root):
    if root is None:
        return 0
    left = sum(root.left)
    right = sum(root.right)

    return left + right + root.value
# print(sum(root))
# ---------------------------------------------------------------------
# Height of a Tree

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    
    heightOfTree = max(left, right) + 1 
    return heightOfTree
# print(height(root))
# ---------------------------------------------------------------------
# Diameter of a Tree - Number of Nodes in the longest path between any 2 nodes 
# Approach 1 : O(N^2)
def diameter(root):
    if root is None:
        return 0
    diam1 = diameter(root.left)
    diam2 = diameter(root.right)
    diam3 = height(root.left) + height(root.right) + 1 
    
    return max(diam3, max(diam1, diam2))
    
# print(diameter(root))
# Approach 2 : O(N)
class TreeInfo:
    def __init__(self, ht, diam):
        self.ht = ht
        self.diam = diam 
def diameter2(root):
    if root is None:
        return TreeInfo(0, 0)
    left = diameter2(root.left)
    right = diameter2(root.right)
    
    height = max(left.ht, right.ht) + 1 
    
    diam1 = left.diam
    diam2 = right.diam 
    diam3 = left.ht + right.ht + 1
    
    diameters = max(max(diam1, diam2), diam3)
    
    myinfo = TreeInfo(height, diameters)
    return myinfo
# print(diameter2(root).diam)

# ---------------------------------------------------------------------
# root =           1
#                 / \
#                2   3
#               / \   \
#              4  5    6
newNodes = [2, 4, -1, -1, 5, -1, -1]
#                2   
#               / \   
#              4  5 
idx = -1
root2 = TreePreorder(newNodes)
            
# Is subtree of main tree problem (amazon, facebook)
def isIdentical(root, subRoot):
    if root == None and subRoot == None:
        return True
    if root == None or subRoot == None:
        return False
    if root.value == subRoot.value:
        return isIdentical(root.left, subRoot.left) and isIdentical(root.right, subRoot.right)

def isSubTree(root, subRoot):
    if subRoot is None:
        return True
    if root is None:
        return False
    
    if root.value == subRoot.value:
        if isIdentical(root, subRoot):
            return True 
    
    return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)

print(isSubTree(root, root2))