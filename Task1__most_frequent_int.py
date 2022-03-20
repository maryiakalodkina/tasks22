#TASK 1:
    #Find the most frequent integer in an array
    #Only positive integers
from random import randint

ARRAY_LENGTH = 10000
#TESTS:
#my_array = [2, 5, 8, 9, 2, 11, 4, 4, 5, 4, 11, 11, 14, 11, 5, 5]
#my_array = [8, 8, 9, 9, 7, 15, 15, 2, 20, 13, 2, 24, 6, 11, 7, 12, 4, 10, 18, 13, 23, 11, 3, 11, 12, 10, 4, 5, 4, 22, 6, 3, 19, 14, 21, 11, 1, 5, 14, 8, 0, 1, 16, 5, 10, 13, 17, 1, 16, 17, 12, 6, 10, 0, 3, 9, 9, 3, 7, 7, 6, 6, 7, 5, 14, 18, 12, 19, 2, 8, 9, 0, 8, 4, 5]
my_array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
#Corner case: what if there are a few integers with the same frequency of appearence

def most_frequent_integer(my_array):
    
    count = 0
    most_freq_int_array = []

    for i in my_array:
        #how many times the integer appears in an array
        amount = my_array.count(i)

        if amount > count:
            
            #first evet integer from array
            if len(most_freq_int_array) == 0:
                most_freq_int_array.append(i)

            #if array is not empty
            else:
                #empty the array as all the previous integer's frequencies of occurence are smaller
                most_freq_int_array.clear()
                most_freq_int_array.append(i)
            
            count = amount
        
        #the integer with the same frequency of occurence was already found
        elif amount == count:
            most_freq_int_array.append(i)
    
    #remove all the dublicates
    most_freq_int_array = list(set(most_freq_int_array))

    return most_freq_int_array

answer = most_frequent_integer(my_array)
print(my_array)
print(answer)


