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

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
print(user)

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))

user = database.find('siddhant')
print(user)

print(database.list_all())

database.insert(biraj)

print(database.list_all())


