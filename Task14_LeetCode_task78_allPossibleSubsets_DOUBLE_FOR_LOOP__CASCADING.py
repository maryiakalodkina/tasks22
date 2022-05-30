#LeetCode task 78 - subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def subsets(nums):
    n = len(nums)
    output = [[]]
        
    for num in nums:
        for curr in output:
            curr = curr + [num]
            output = output + [curr]
        
    return output

theArray = [1,2,3]
answer = subsets(theArray)
print(answer)

