#TASK 9: traversing matrix spirally
# first row -> last column -> last row -> first column -> etc.

def traversingMatrix(my_matrix):
    answ_list = []

    rows = len(my_matrix)  #3
    columns = len(my_matrix[0]) #3
    beg_r = 0
    beg_c = 0

    while (beg_r < rows or beg_c < columns):
        for i in range (beg_c, columns):
            print(my_matrix[beg_r][i])				#1, 2, 3
            answ_list.append(my_matrix[beg_r][i])
        beg_r += 1

        for j in range (beg_r, rows):
            print(my_matrix[j][columns-1]) 				#6, 9
            answ_list.append(my_matrix[j][columns-1])
        columns -= 1

        if (beg_r<rows):
            for k in range(columns-1, beg_c-1, -1):
                print(my_matrix[rows-1][k])				#8, 7
                answ_list.append(my_matrix[rows-1][k])
            rows -= 1

        if(beg_c<columns):
            for l in range(rows-1, beg_r-1, -1):
                print(my_matrix[l][beg_c])				#4
                answ_list.append(my_matrix[l][beg_c])
            beg_c += 1


    return answ_list


# Input: 
#my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 
# [1,2,3,6,9,8,7,4,5]

# Input: 
my_matrix = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

answer = traversingMatrix(my_matrix)
print(answer)