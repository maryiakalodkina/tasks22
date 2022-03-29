# TASK 3:
# Given an unsorted array of positive integers, determine if any two numbers in the array add to 100
# Example: [1, 2, 4, 50] - false; [1, 4, 96, 65, 30] - true

from random import randint

ARRAY_LENGTH = 10000
#TESTS:
#my_array = [2, 5, 8, 9, 2, 11, 4, 4, 5, 4, 11, 11, 14, 11, 5, 5]
my_array = [8, 8, 9, 9, 7, 15, 15, 2, 20, 13, 2, 24, 6, 11, 7, 10, 4, 5, 4, 22, 6, 3, 19, 14, 11, 1, 5, 14, 8, 0, 1, 16, 5, 10, 13, 17, 1, 16, 17, 12, 6, 10, 0, 3, 9, 9, 3, 7, 7, 6, 6, 7, 5, 14, 18, 12, 19, 2, 8, 9, 0, 8, 4, 5]
#my_array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
#Corner case: what if there are a few integers with the same frequency of appearence

def add_to_hundred (my_array):
    
    for i in my_array:
        x = 100 - i
        if x in my_array: return True

    return False

answer = add_to_hundred(my_array)
print(answer)