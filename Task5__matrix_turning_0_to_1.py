# TASK 5: 
# Matrix: turning 0s to 1s 

def turning_zeros_to_ones(zero_matrix):

    ''' f - first index of the raw
        c - last index of the raw
        s - first index of the column
        r - last index of the column'''

    #how many raws
    r = len(zero_matrix)
    #how many columns
    c = len(zero_matrix[0])

    f = 0
    s = 0

    #new matrix we will return
    one_matrix = [[0 for col in range(c)] for raw in range(r)]
    
    print('Initial matrix:')
    for ch in range(s, r):
        print(zero_matrix[ch])
    
    #goint through all the raws
    for i in range(s, r):
        #goint through all the columns
        for j in range(f, c):
            #if we see any 1s
            if zero_matrix[i][j] == 1:
                #number of the raw to be turned to 1
                raw = i
                #number of the column to be turned to 1
                column = j

                #turn the whole raw i to ones in one_matrix
                for m in range(f, c):
                    one_matrix[i][m] = 1
                #turn the whole raw i to ones in one_matrix
                for n in range(s, r):
                    one_matrix[n][j] = 1
    
    print()
    print('New matrix:')
    for th in range(s, r):
        print(one_matrix[th])

    return one_matrix


new_matrix = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]
answer = turning_zeros_to_ones(new_matrix)



        
