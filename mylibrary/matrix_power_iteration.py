'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task1
course:             Math 5610

purpose:            This method will find the largest eigenvector of a metrix using the power iteration
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose


def matrix_power_iteration(matrix,tol,max_iter):
    error = tol * 10
    count = 0
    eigenvaluenew = 1
    v_i = convert_vec_mat(matrix[0])
    while error > tol and count < max_iter:
        eigenvalueold = eigenvaluenew
        v_i = matrix_mult(matrix, v_i)
        v_i = matrix_scal_mult(1/vector_2norm(convert_vec_mat(v_i)),v_i)
        eigenvaluenew = matrix_mult(matrix_transpose(v_i),matrix_mult(matrix,v_i))[0][0]
        count += 1
        error = abs(eigenvaluenew - eigenvalueold)
    return eigenvaluenew

#The code below is used just for testing.
#matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
#print(matrix_power_iteration(matrix_example,0.00000001,1000))


