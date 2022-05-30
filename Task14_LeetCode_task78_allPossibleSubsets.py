#LeetCode task 78 - subsets

# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def subsets(nums):
        output = []
        path = []
        
        def helper(index, path):
            
            if index == len(nums):
                baseCase = path.copy()
                output.append(baseCase)
                return
        
            #RECURSIVE CALLS:
            
            #exclusion
            helper(index+1, path)
            
            #inclusion
            m = nums[index]
            path.append(m)
            helper(index+1, path)
            path.remove(m)
            
        helper(0, path)
            
        return output

theArray = [1,2,3]
answer = subsets(theArray)
print(answer)