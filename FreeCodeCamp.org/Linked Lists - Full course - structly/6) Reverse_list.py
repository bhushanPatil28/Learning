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

def reverse(head):
    prev = None
    current = head
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# def reverse(head, prev = None):
#     if head ==None:
#         return prev
#     next = head.next
#     head.next = prev
#     return reverse(next, head)
    

def linkedListValues(head):
    values = []
    fillValues(head, values)
    return values

def fillValues(head, values):
    if head is None:
        return
    values.append(head.val)
    fillValues(head.next, values)

reversed_head = reverse(a)
reversed_values = linkedListValues(reversed_head)
print(reversed_values)