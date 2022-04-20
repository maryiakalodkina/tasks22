# TASK 8: reverse a positive integer

#FIRST APPROACH:
#through list
def reverseIntFirstApproach(givenInt):
    
    #converting int to list of strings:
    result = [str(x) for x in str(givenInt)]
    #reversing the list
    result.reverse()
    #combining the elements of list in one string and turning it back to int
    result = int(''.join(result))
    
    return result

#SECOND APPROACH:
#through string
def reverseIntSecondApproach(givenInt):

    #converting int to a string, reversing it and turning back to int
    result2 = int(''.join(reversed(str(givenInt))))
    
    return result2

#THIRD APPROACH:
# mathematical approach
def reverseIntThirdApproach(givenInt):

    result3 = 0
    while (givenInt > 0):
        result3 = (result3 * 10) + (givenInt % 10)
        givenInt = (givenInt // 10)

    return result3

#FORTH APPROACH:
#mathematical with recursion 
def reverseIntFourthApproach(givenInt, result4):
    
    result4 = (result4 * 10) + (givenInt % 10)
    givenInt = (givenInt // 10)

    # print('givenInt is {} and result4 is {}'.format(givenInt, result4))

    if givenInt > 0:
        return reverseIntFourthApproach(givenInt, result4)
    else:
        # print(result4)
        return result4


new_int = 12345
answer = reverseIntFirstApproach(new_int)
answer2 = reverseIntSecondApproach(new_int)
answer3 = reverseIntThirdApproach(new_int)
answer4 = reverseIntFourthApproach(new_int, 0)
