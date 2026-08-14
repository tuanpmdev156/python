def pretty_print(A):
    size = 2*A-1
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    # Create 4 pointers
    top = 0
    bottom = size - 1
    start = 0
    end = size
    
    # Loop to fill in
    while (A > 0):
        for i in range(start,end):
            matrix[top][i] = A
            matrix[bottom][i] = A

        for j in range(top, end):
            matrix[j][bottom] = A
            matrix[j][top] = A
        #for k in range(start,end):
        #    matrix[bottom][k] = A

        #for h in range(top,end):
        #    matrix[h][top] = A
        top += 1
        start +=1
        end -=1
        bottom -=1
        A -= 1
    print(matrix)
    
pretty_print(3)

