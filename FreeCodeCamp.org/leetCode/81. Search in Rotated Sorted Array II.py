# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 



# Since the array is given in a sorted order, so it can be solved using the binary search algorithm.

# To solve this problem we have to follow the folllowing steps:

# Calculate the mid index.
# Check if the mid element == target, return True else move to next step.
# Else if the mid element >= left.
# if mid element >= target and and left <= target, then shift right to mid-1 position, else shift left to mid+1 position.
# Else,
# If target >= mid element and target <=right, then shift left to mid+1 position, else shift right to mid-1 position.
# If the element is not found return False
# Note: Since duplicate elemnts are present in the array so remove all the duplicates before step step 1.
# To remove duplicate,

# Shift left while left == left+1, and
# Shift right while right == right-1.

# If the length of the given array list is 1, then check the first element and return accordingly
def search(nums, target):

    if len(nums)==1:
        if nums[0]!=target:
            return False
        else:
            return True

    left=0
    right=len(nums)-1
    # binary search 
    while(left<=right):

        # shifting to remove duplicate elements
        while left<right and nums[left] == nums[left+1]:
            left+=1
        while left<right and nums[right] == nums[right-1]:
            right-=1

        # step 1 calculate the mid    
        mid=(left+right)//2

        #step 2
        if nums[mid]==target:
            return True

        #step 3
        elif nums[left]<=nums[mid]:
            if nums[mid]>=target and nums[left]<=target:
                right=mid-1
            else:
                left=mid+1

        # step 4
        else:
            if target>=nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1

    # step 5
    return False

