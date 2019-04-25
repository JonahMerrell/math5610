'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 11 2019
written for:        Homework6 Task3
course:             Math 5610

purpose:            This method will find the solution of a matrix using a least squares technique with QR factorization.
https://math.la.asu.edu/~gardner/QR.pdf
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_outer, matrix_add, matrix_scal_mult, vector_dot, vector_scal_mult, vector_add, vector_2norm, matrix_mult

def matrix_QR_factorization_householder(matrix):
    matrix_R = [[matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))] #HA starts by being A
    matrix_Q = [[0 for j in range(len(matrix))] for k in range(len(matrix))] #Q starts by being the identity matrix

    for j in range(len(matrix)):
        matrix_Q[j][j] = 1
    for i in range(len(matrix[0])-1):
        a = [matrix_R[j][i] for j in range(len(matrix_R))] #a is the i'th column of matrix_R, with 0s inserted above the diagonal
        for j in range(i):
            a[j] = 0
        r = [0]* len(a) #r is just a 0 vector, with the i'th column being the magnitude of a
        r[i] = vector_2norm(a)
        u = vector_add(a,vector_scal_mult(-1,r))
        i_ = [[0 for j in range(len(matrix))] for k in range(len(matrix))]
        for j in range(len(matrix)):
            i_[j][j] = 1
        if vector_dot(u,u) != 0:
            h = matrix_add(i_,matrix_scal_mult(-2/vector_dot(u,u),matrix_outer(u, u))) #computer h_i
        else: #if u ends up being the 0 matrix, then h is just the identity matrix
            h = i_
        matrix_Q = matrix_mult(matrix_Q,h)
        matrix_R = matrix_mult(h,matrix_R)
    #matrix_R = matrix_R[:len(matrix_R[0])] #technically, R is a 3x3 matrix, since the 4th row is just 0s.

    return [matrix_Q, matrix_R]

#The code below is used just for testing.
#matrix_example = [[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]]
#matrix_new = matrix_QR_factorization_householder(matrix_example)
#for i in range(0,len(matrix_new[0])):
#    print(matrix_new[0][i])
#for i in range(0,len(matrix_new[1])):
#    print(matrix_new[1][i])
#print(matrix_mult(matrix_new[0],matrix_new[1]))
