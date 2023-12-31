class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(5)
c = Node(9)
d = Node(15)

a.next = b
b.next = c
c.next = d

# # with loop
# def linkedListValues(head):
#     values = []
#     current = head
#     while(current!=None):
#         values.append(current.val)
#         current = current.next
#     return values

# print(linkedListValues(a))

# # with recursion (my version)
# values = []
# def linkedListValues(head):
#     if head is None:
#         return
#     values.append(head.val)
#     linkedListValues(head.next)

# linkedListValues(a)
# print(values)

# video version of recursion
def linkedListValues(head):
    values = []
    fillValues(head, values)
    return values

def fillValues(head, values):
    if head is None:
        return
    values.append(head.val)
    fillValues(head.next, values)

print(linkedListValues(a))


