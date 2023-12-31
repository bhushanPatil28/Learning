# This program uses binary search

def locate_card(cards, query):
    if query == None:
        return -1
    lo, hi = 0, len(cards)-1
    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = cards[mid]
        
        if mid_number == query:
            return mid 
        elif mid_number < query:
            lo = mid + 1
        elif mid_number > query:
            hi = mid - 1
    return -1 

# Test cases

tests = []

# Element at the last
tests.append({
    'input':{
        'cards': [1,2,3,4,8,9,10],
        'query': 10
    },
    'output':6
})

# Element in the middle
tests.append({
    'input':{
        'cards': [1,2,3,4,8,9,10],
        'query': 4
    },
    'output':3
})

# Element at the start
tests.append({
    'input':{
        'cards': [1,2,3,4,8,9,10],
        'query': 1
    },
    'output':0
})

# Element not present
tests.append({
    'input':{
        'cards': [1,2,3,4,8,9,10],
        'query': 52
    },
    'output':-1
})

# Query is not provided
tests.append({
    'input':{
        'cards': [1,2,3,4,8,9,10],
        'query': None
    },
    'output':-1
})

for result in tests:
    print(locate_card(**result['input'])==result['output'])

print(locate_card([1,2,4,6,8,10], 10))