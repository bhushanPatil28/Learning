class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)

a.next = b
b.next = c
c.next = d


# freeCodeCamp version of recursive
def sumList(head):
    if head is None:
        return 0
    return head.val + sumList(head.next)

print(sumList(a))

# # Solved my self (loop method)
# def sumList(head):
#     current = head
#     sum_of_list = 0
#     while current != None:
#         sum_of_list += current.val
#         current = current.next
#     return sum_of_list

# print(sumList(a))

# cannot able to do recursively
# # def sumList(head):
# #     sum_of_list = 0
# #     calculate(head, sum_of_list)
# #     return sum_of_list

# # def calculate(head, sum_of_list):
# #     if head is None:
# #         return 0
# #     sum_of_list = sum_of_list + head.val
# #     calculate(head.next, sum_of_list)

# # print(sumList(a))