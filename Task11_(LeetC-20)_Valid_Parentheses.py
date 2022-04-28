# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

def isValid(s):
        
        tempArray = []
        if len(s) % 2 == 0:
            for element in s:
                if element == '(' or element == '{' or element == '[':
                    tempArray.append(element)
                elif tempArray:
                    if element == ')' and tempArray[-1] == '(':
                        del tempArray[-1]
                    elif element == '}' and tempArray[-1] == '{':
                        del tempArray[-1]
                    elif element == ']' and tempArray[-1] == '[':
                        del tempArray[-1]
                    else:
                        break
                else:
                    return False	
        else:
            return False
        
        if tempArray:
            return False
        else:
            return True

answer = isValid("()[]{}]")
print(answer)