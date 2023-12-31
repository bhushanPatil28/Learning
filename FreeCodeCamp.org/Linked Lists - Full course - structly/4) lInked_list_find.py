class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('M')
b = Node('A')
c = Node('Y')
d = Node('U')
e = Node('R')

a.next = b
b.next = c
c.next = d
d.next = e

# def find(head, target):
#     current = head
#     while current != None:
#         if current.val == target:
#             return True
#         current = current.next
#     return False

def find(head, target):
    if head is None:
        return False
    if head.val == target:
        return True
    return find(head.next, target)

print(find(a, 'A'))
        
