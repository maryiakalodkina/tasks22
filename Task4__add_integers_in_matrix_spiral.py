# TASK 4:
# Add all the integers in the matrix 4x4 in a spiral form starting with the first column


def add_matrix(matrix):

    ''' f - first index of the raw
        l - last index of the raw
        s - first index of the column
        t - last index of the column'''
    
    f = 0
    s = 0
    l = len(matrix[0])
    t = len(matrix)

    print('l is {} and t is {}'.format(l,t))

    sum = 0

    while((f<l) and (s<t)):

        #traversing the first column
        for i in range(s, t):
            print(matrix[i][f])
            sum += matrix[i][f]
        f+=1

        #traversing the last raw
        for i in range(f, l):
            print(matrix[t-1][i])
            sum += matrix[t-1][i]
        t-=1

        #traversing the last column
        if(f<l):
            for i in range(t-1, s-1, -1):
                print(matrix[i][(l-1)])
                sum += matrix[i][(l-1)]
            l-=1
        
        #traversing the first raw
        if(s<t):
            for i in range(l-1, (f-1), -1):
                print(matrix[s][i])
                sum += matrix[s][i]
            s+=1

    return sum

new_matrix = [[2, 3, 4, 5], [14, 8, 11, 9], [3, 14, 48, 5], [23, 29, 4, 6]] # 4x4

''' 
    2           3   <-    4    <-   5
    |           |                   ^
    v           v                   |
    14          8        11         9
    |           |        ^          ^
    v           v        |          |             
    3           14   ->  48         5
    |                               ^
    v                               |
    23    ->    29   ->  4   ->     6
    
    '''


answer = add_matrix(new_matrix)
print(answer)