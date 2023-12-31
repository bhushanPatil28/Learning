from jovian.pythondsa import evaluate_test_case
from jovian.pythondsa import evaluate_test_cases



def locate_card(cards, query):
    # Create a variable position with the value 0 
    position = 0 
    
    # set up a loop for repetition
    while position<len(cards):
        
        # Check if element at the current position match the query
        if cards[position] == query:
            
            # Answer found! Return and exit...
            return position
        position += 1 
        
        # Check if we have reached the end of the array 
        if position >= len(cards):
            
            # Number not found, return -1 
            return -1 
    pass


# first test case 
test = {
    'input': {
        'cards': [13,11,10,7,4,3,1,0],
        'query': 7 
    },
    'output': 3
}

print(locate_card(**test['input']) == test['output'])

tests = []

tests.append(test)

# query occurs in some where in the middle 
tests.append({
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query': 1
    },
    'output': 6
})
# query is the first element
tests.append({
    'input': {
        'cards': [4,2,1,-1],
        'query': 4
    },
    'output': 0 
})
# query is the last element
tests.append({
    'input': {
        'cards': [3,-1,-9,-127],
        'query': -127
    },
    'output': 3
})
# cards constains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})


# We will assume that out function will return -1 in case cards does not contain query 

# cards does not conntain query 
tests.append({
    'input':{
        'cards': [9,7,5,2,-9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input':{
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input':{
        'cards':[8,8,6,6,6,6,3,2,2,2,0,0,0],
        'query': 3
    },
    'output': 7 
})

# query occurs multiple times
tests.append({
    'input':{
        'cards':[8,8,6,6,6,6,3,2,2,2,0,0,0],
        'query': 6
    },
    'output': 2 
})

# print(tests)
evaluate_test_cases(locate_card, tests)