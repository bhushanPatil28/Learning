def locate_card(cards, query):
    if len(cards) == 0:
        return -1
    position = 0

    while position<len(cards):
        if cards[position] == query:
            return position
        position+=1
        if position == len(cards):
            return -1 
    # pass


# test cases

tests = []

# query somewhere in the middle
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7,8],
        'query': 7
    },
    'output': 6
})

# query at the start
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7,8],
        'query': 1
    },
    'output': 0
})

#query at the end
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7,8],
        'query': 8
    },
    'output': 7
})

# query not in the cards
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7,8],
        'query': 9
    },
    'output': -1
})

# cards list is empty
tests.append({
    'input':{
        'cards': [],
        'query': 1
    },
    'output': -1
})

# query is empty
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7,8],
        'query': None
    },
    'output': -1
})

# multiple query return first encountered
tests.append({
    'input':{
        'cards': [1,2,2,3,3,4,4,4,5,6,7,8],
        'query': 4
    },
    'output': 5
})

for result in tests:
    # print(result['input'])
    print(locate_card(**result['input']) == result['output'])
