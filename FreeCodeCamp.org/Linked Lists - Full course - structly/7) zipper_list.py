class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
# first Lnked list
a = Node('M')
b = Node('A')
c = Node('Y')
d = Node('U')
e = Node('R')

a.next = b
b.next = c
c.next = d
d.next = e

# second linked list
f = Node(1)
g = Node(2)
h = Node(3)

f.next = g
g.next = h 

def zipper(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 != None and current2 != None:
        # print(f"tail = {tail.val}, current1 = {current1.val}, current2 = {current2.val}")
        if count%2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        tail = tail.next
        count += 1

        if current1 != None:
            tail.next = current1
        if current2 != None:
            tail.next = current2
    return head1

# # recursive
# def zipper(head1, head2):
#     if head1 == None and head2 == None:
#         return None
#     if head1 == None:
#         return head2
#     if head2 == None:
#         return head1
    
#     next1 = head1.next
#     next2 = head2.next
#     head1.next = head2;
#     head2.next = zipper(next1, next2)
#     return head1

zipper(a, f)
