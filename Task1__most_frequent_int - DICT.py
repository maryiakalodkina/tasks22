#TASK 1:
    #Find the most frequent integer in an array
    #Only positive integers

#Time_complexity: n (to got through array) * n (to find the highest value in dictionary) * n (to collect all the keys with the highest value) => O(3n)
#Space complexity: 

from random import randint

ARRAY_LENGTH = 10000
#TESTS:
#my_array = [2, 5, 8, 9, 2, 11, 4, 4, 5, 4, 11, 11, 14, 11, 5, 5]
#my_array = [8, 8, 9, 9, 7, 15, 15, 2, 20, 13, 2, 24, 6, 11, 7, 12, 4, 10, 18, 13, 23, 11, 3, 11, 12, 10, 4, 5, 4, 22, 6, 3, 19, 14, 21, 11, 1, 5, 14, 8, 0, 1, 16, 5, 10, 13, 17, 1, 16, 17, 12, 6, 10, 0, 3, 9, 9, 3, 7, 7, 6, 6, 7, 5, 14, 18, 12, 19, 2, 8, 9, 0, 8, 4, 5]
my_array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
#Corner case: what if there are a few integers with the same frequency of appearence

def most_frequent_integer(my_array):
    
    my_dict = {}
    most_freq_int_array = []

    #creating a dictionary where all the integers from arrays are keys and their frequencies are values
    for i in my_array:

        if i in my_dict.keys():
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    
    #finding the maximum value (the highest frequency of occurance))
    highest_val = max(my_dict.items(), key=lambda x:x[1])

    #collect all the keys (integers) that have the same highest value (frequency of occurance)
    for key, value in my_dict.items():

        if value == highest_val[1]:
            most_freq_int_array.append(key)

    return most_freq_int_array

answer = most_frequent_integer(my_array)
print(answer)


