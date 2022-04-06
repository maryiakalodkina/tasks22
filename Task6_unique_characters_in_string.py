# TASK 6: Verify that given string has only unique chars (spaces are not included)

# Corner case: what if the string contains not only letters
# Corner case: what if the string is empty

my_dict = {}

def only_unique_chars(my_string):

    split_string = list(my_string)
    print(split_string)
    for i in split_string:
        print(i)
        if i.isspace() == True:
            pass
        elif i in my_dict.keys():
            return False
        else:
            my_dict[i] = 1

    return True

    
#my_string = 'I had breakfast today 34'
my_string = 'Hey, 48 :)'
#my_string = []
answer = only_unique_chars(my_string)
print(answer)


