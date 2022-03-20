#TASK 2:
    #There are 2 sorted in ascending order arrays
    #Combine them to get a new sorted array
    #Only positive integers

from random import randint
ARRAY_LENGTH = 300

#array1 = [2, 2, 4, 4, 4, 5, 5, 5, 5, 8, 9, 11, 11, 11, 11, 14]
#array2 = [1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 10, 10, 11, 11, 11, 11, 12, 12, 13, 13, 14, 14, 16, 18, 19, 20, 21, 22, 23, 24]

array1 = sorted([randint(0, 1000) for i in range(ARRAY_LENGTH)])
array2 = sorted([randint(0, 1000) for i in range(ARRAY_LENGTH)])

def combine_array(array1, array2):

    combined_array = []

    while len(array1) > 0 and len(array2) > 0:

        ptr1 = array1[0]
        ptr2 = array2[0]

        if ptr1 < ptr2:
            combined_array.append(ptr1)
            del array1[0]
        elif ptr1 > ptr2:
            combined_array.append(ptr2)
            del array2[0]
        elif ptr1 == ptr2:
            combined_array.append(ptr1)
            del array1[0]

    if len(array1) == 0:
        combined_array = combined_array + array2
    elif len(array2) == 0:
        combined_array = combined_array + array1

    return combined_array

answer = combine_array(array1, array2)


