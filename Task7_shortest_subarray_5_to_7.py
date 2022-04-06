# TASK 7: Find the shortest subarray starts with 5 and ends with 7

# a1 = []   # in this case it will return an empty array
# a2 = [3,5,5,7,8,5,9,11,7]
# a3 = [3,5,7,0,7,8]
a4 = [3,4,5,5,6,9,7,3,5,6,9,7]  #in this situation it will return the first similar array
# a5 = [4,12,49,3,9,15]

def shortest_subarray (arr):

    result = []
    temp_array = []
    size = len(arr)
    
    #traversing through array
    for i in range(0, (len(arr)-1)): # from 0 to 5 in a3
        
        #the beginning of an subarray
        if arr[i] == 5:

            temp_array.clear()
            # traversing through possible subarray
            for index in range(i,(len(arr))):          
                temp_array.append(arr[index])

                #the end of an subarray
                if arr[index] == 7:
                    break

        # checking if this temp_array is the smallest one we had so far
        # if yes, then update the result array with this temp_array's elements
        if (len(temp_array) < size) and (len(temp_array) > 0):
            result.clear()
            size = len(temp_array)
            for a in range(0, len(temp_array)):   
                num = temp_array[a]
                result.append(num)

    return result

answer = shortest_subarray(a4)
print(answer)