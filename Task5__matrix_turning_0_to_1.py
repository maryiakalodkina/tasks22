# TASK 5: 
# Matrix: turning 0s to 1s 

def turning_zeros_to_ones(zero_matrix):

    ''' f - first index of the row
        c - last index of the row
        s - first index of the column
        r - last index of the column'''

    #how many rows
    r = len(zero_matrix)
    #how many columns
    c = len(zero_matrix[0])

    f = 0
    s = 0

    array_rows = []
    array_cols = []
    
    print('Initial matrix:')
    for ch in range(s, r):
        print(zero_matrix[ch])
    
# STEP 1: Figuring out what rows and columns have to be turned to 1s

    #goint through all the rows
    for i in range(s, r):
        #goint through all the columns
        for j in range(f, c):
            #if we see any 1s
            if zero_matrix[i][j] == 1:
                #number of the row to be turned to 1
                row = i
                #number of the column to be turned to 1
                column = j

                array_rows.append(i)
                array_cols.append(j)

    #removing dublicates in both and sorting
    rows = sorted(list(set(array_rows)))          
    columns = sorted(list(set(array_cols)))        

    point_r = 0
    point_c = 0

    # STEP 2: Turning specific rows and columns to 1s

    #goint through all the rows
    for k in range(s, r):
        #goint through all the columns
        for l in range(f, c):
            if ((point_r < (len(rows)) and (k == rows[point_r]))):
                #turn the whole row k to ones in zero_matrix
                for m in range(f, c):
                    zero_matrix[k][m] = 1
                point_r += 1
            if  (point_c < (len(columns))) and ((l == columns[point_c])):
            #turn the whole column l to ones in zero_matrix
                for n in range(s, r):
                    zero_matrix[n][l] = 1     
                point_c += 1          

    print()
    print('New matrix:')
    for th in range(s, r):
        print(zero_matrix[th])

    return zero_matrix

new_matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
answer = turning_zeros_to_ones(new_matrix)
