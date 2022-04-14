def reverse_int (my_int):
    output = 0
    while (my_int>10):
        output = (output *10) + (my_int% 10)
        my_int = (my_int // 10)
  

    return 0

new_int = 12345
output = reverse_int(new_int)
print(output)
