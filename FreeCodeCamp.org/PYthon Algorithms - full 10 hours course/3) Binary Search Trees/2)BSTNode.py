class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

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
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name 
        self.email = email 
        print("user Created") 

    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"
    
    def __str__(self):
        return self.__repr__()
    

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break 
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user 

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users
    

database = UserDatabase()

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

   
tree =insert(None, jadhesh.username, jadhesh)
print(tree.key, tree.value)

insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, vishal)

BSTNode.display_keys(tree)




# FINDING NODE key

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    
# found = find(tree, 'sonaksh')
# print(found.key, found.value)




# Updating a value in a BSt

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

# before updating
found = find(tree, 'hemanth')
print(found.value)

update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj0@example.com'))

# After updating
found = find(tree, 'hemanth')
print(found.value)




# list the nodes
# QUESTION - Write a function to retrieve all the key-values pairs stored in BST in the sorted order of keys

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
print(list_all(tree))