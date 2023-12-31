from jovian.pythondsa import evaluate_test_cases

# def find_rotation(nums):
#     if len(nums) == 0:
#         return -1
#     if nums == sorted(nums):
#         return 0
#     rotations = 0
#     if nums[0] < nums[1]:
#         for i in range(len(nums)):
#             if nums[i] < nums[i+1]:
#                 rotations += 1
#             elif nums[i] == nums[len(nums)-1]:
#                 return 0
#             elif nums[i] > nums[i+1]:
#                 break 
#     elif nums[0] > nums[1]:
#         for i in range(len(nums)):
#             if nums[i] > nums[i+1] and nums[i] >= nums[i+1]+1 :
#                 rotations += 1
#             elif nums[i] == nums[len(nums)-1]:
#                 return 0
#             elif nums[i] < nums[i+1]:
#                 break 
#     return rotations+1


# used chat gpt to get 0(logn) complexity
def find_rotation(nums):
    if len(nums) == 0:
        return -1
    
    lo, hi = 0, len(nums)-1

    while lo<hi:
        mid = lo + (hi-lo)//2

        if nums[mid] > nums[hi]:
            lo = mid+1
        else:
            hi = mid 
    return lo

# test cases 

tests = []

# Normal case
tests.append({
    'input':{
        'nums':[6,7,8,1,2,3,4,5]
    }, 
    'output': 3
})


tests.append({
    'input':{
        'nums':[4,5,6,7,8,1,2,3]
    }, 
    'output': 5
})

# minus case
tests.append({
    'input':{
        'nums':[0,1,2,3,-10,-8,-5,-1]
    }, 
    'output': 4
})

tests.append({
    'input':{
        'nums':[5,6,7,8,9,10]
    }, 
    'output': 0
})

tests.append({
    'input':{
        'nums':[]
    }, 
    'output': -1
})



tests.append({
    'input':{
        'nums':[9, 8, 7, 6, 5, 1, 2, 3, 4]
    }, 
    'output': 5
})


# print(evaluate_test_cases(find_rotation, tests))
for result in tests:
    print(find_rotation(**result['input']) == result['output'])
