from jovian.pythondsa import evaluate_test_cases

def locate_card(cards, query):
    lo, hi = 0, len(cards) -1
    if query == None:
        return -1

    while lo <= hi:
        mid = (lo+hi)//2     #does not return decimle
        mid_number = cards[mid]

        print("lo:", lo, ", hi:", hi, ",mid:", mid, "mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number > query: 
            hi = mid - 1
        elif mid_number < query: 
            lo = mid + 1
    return -1


# test cases

tests = []

# Check for element in middle somewhere
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7],
        'query': 5
    },
    'output': 4
})

#tests middle element
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7],
        'query': 4
    },
    'output': 3
})

# tests empty list
tests.append({
    'input':{
        'cards': [],
        'query': 5
    },
    'output': -1
})

# checks if query not provided
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7],
        'query': None
    },
    'output': -1
})

# checks if query is not present
tests.append({
    'input':{
        'cards': [1,2,3,4,5,6,7],
        'query': 9
    },
    'output': -1
})

# checks for multiple first occurence    (new fix in fine new_approach.py)
tests.append({
    'input':{
        'cards': [8,8,6,6,6,6,6,6,5,5,3,2,2,1,0],
        'query': 6
    },
    'output': 2
})

evaluate_test_cases(locate_card, tests)