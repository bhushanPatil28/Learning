import math
cards = [13, 11, 10, 7, 4, 3, 1]
query = 7 
output = 3

def locate_card(cards, query):
    for i in range(len(cards)-1):
        if cards[i] == query:
            return i


tests = []

# middle
tests.append({
    'input' : {
        'cards': [13, 11, 10, 7, 4, 3, 1],
        'query' : 7
    },
    'output' : 3
})

# first
tests.append({
    'input' : {
        'cards' : [4, 2, 1,  -1],
        'query' : 4
    },
    'output' : 0
})

# last
tests.append({
    'input' : {
        'cards' : [3, -1, -9, -127],
        'query' : -127
    },
    'output' : 3
})

# one element
tests.append({
    'input' : {
        'cards' : [6],
        'query' : 6
    },
    'output' : 0
})

# not contain
tests.append({
    'input' : {
        'cards' : [9, 7, 5, 2, -9],
        'query' : 4
    },
    'output' : -1
})

# empty
tests.append({
    'input' : {
        'cards' : [],
        'query' : 7
    },
    'output' : -1
})

# repeat in cards
tests.append({
    'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 3
    },
    'output' : 7
})

# occcrus multiple times
tests.append({
    'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query' : 6
    },
    'output' : 2
})

for i in tests:
    print(i)

# print(locate_card(**tests['input']) == tests['output'])