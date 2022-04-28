#Task 10: sum two numbers given as array of digits
#100+1=101
#input [1,0,0], [1] ->  []
#output [1,0,1]

def sumInts(arr1, arr2):
    output = []
    extraOne = False

    length = len(arr1) - len(arr2)
    if length > 0:
        for i in range (0, length):
            arr2.insert(i, 0)
    else:
        for i in range (0, abs(length)):    # |length|
            arr1.insert(i, 0)

    num1 = arr1[::-1] 
    num2 = arr2[::-1] 

    for i in range (0, len(num1)):	
        num = num1[i] + num2[i]
        if extraOne == True:
            num += 1
            extraOne = False

        if num > 9:
            extraOne = True
            output.append(num % 10) 
        else:
            output.append(num)

    if extraOne == True:
        output.append(1)
        
    return output[::-1]

answer = sumInts([6,0], [1,6,6])
print(answer)
