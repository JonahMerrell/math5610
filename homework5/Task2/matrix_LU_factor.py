'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 26 2019
written for:        Homework5 Task2
course:             Math 5610

purpose:            This method will return the LU-factorization of a square matrix.
'''
import copy

def matrix_LU_factor(matrix):
    n = len(matrix)
    u_matrix = copy.deepcopy(matrix)
    l_matrix = [[0 for i in range(n)] for j in range(n)]
    for k in range(0,n):
        for i in range(k+1, n):
            l_matrix[i][k] = u_matrix[i][k] / u_matrix[k][k]
            for j in range(k + 1, n):
                u_matrix[i][j] -= l_matrix[i][k]*u_matrix[k][j]
    for i in range(n):
        l_matrix[i][i] = 1.0
    for i in range(1,n):
        for j in range(0, i):
            u_matrix[i][j] = 0.0

    return [l_matrix,u_matrix]


#The code below is used just for testing.
#matrix = [[1.0,1.0,-1.0],[1.0,-2.0,3.0],[2.0,3.0,1.0]]
#matrix_new = matrix_LU_factor(matrix)
#for i in range(0,len(matrix)):
#    print(matrix_new[0][i])
#for i in range(0,len(matrix)):
#    print(matrix_new[1][i])