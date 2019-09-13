'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       Match 4 2019
written for:        Homework5 Task4
course:             Math 5610

purpose:            Implement a method that will generate a symmetric, positive definite matrix.
'''
import random
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_mult, gen_sym_posdef_matrix

def matrix_cholesky_fac(matrix):
    width = len(matrix)
    L_matrix = [[0 for i in range(width)] for j in range(width)]
    for k in range(0, width):
        for i in range(0, k):
            temp_sum = matrix[k][i]
            for j in range(0, i):
                temp_sum -= L_matrix[i][j] * L_matrix[k][j]
            L_matrix[k][i] = temp_sum/L_matrix[i][i]

        temp_sum = matrix[k][k]
        for j in range(0,k):
            temp_sum -= pow(L_matrix[k][j],2)
        L_matrix[k][k] = pow(temp_sum,0.5)

    return L_matrix

#The code below is used just for testing.
#A_ = matrix_cholesky_fac(gen_sym_posdef_matrix())
#A_ = matrix_cholesky_fac([[6,15,35],[15,55,225],[55,225,979]])
#for i in range(len(A_)):
#    print(A_[i])
