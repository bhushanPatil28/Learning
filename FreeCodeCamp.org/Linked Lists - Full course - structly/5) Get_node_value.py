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

def getNodeValue(head, target):
    count = 0
    current = head
    while current != None:
         if count == target:
             return current.val
         current = current.next
         count += 1
    return None
    
# def getNodeValue(head, target):
#     if head is None:
#         return None
#     if target == 0:
#         return head.val
#     return getNodeValue(head.next, target-1)

print(getNodeValue(a, 0))
print(getNodeValue(a, 1))
print(getNodeValue(a, 2))
print(getNodeValue(a, 3))
print(getNodeValue(a, 4))
print(getNodeValue(a, 8))