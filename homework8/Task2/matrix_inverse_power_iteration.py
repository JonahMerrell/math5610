'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task2
course:             Math 5610

purpose:            This method will find the smallest eigenvector of a matrix using the power iteration. Additinally, this
                    method can find any eigenvalue inbetween by using shifting.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose, matrix_solve_LU, matrix_add


def matrix_inverse_power_iteration(matrix,alpha,tol,max_iter,getIterCount=False):
    error = tol * 10
    count = 0
    eigenvaluenew = 0
    I = [[-int(i == j)*alpha for i in range(len(matrix))] for j in range(len(matrix))]
    v_i = matrix[0]
    while error > tol and count < max_iter:

        eigenvalueold = eigenvaluenew
        v_i = matrix_solve_LU(matrix_add(matrix,I),v_i)
        v_i = vector_scal_mult(1/vector_2norm(v_i),v_i)
        eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)),matrix_mult(matrix,convert_vec_mat(v_i)))[0][0]
        count += 1
        error = abs(eigenvaluenew - eigenvalueold)
    if getIterCount == True:
        return eigenvaluenew,count
    else:
        return eigenvaluenew


#The code below is used just for testing.
#matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
#matrix_example = [[-16,9,0,0],[-12,5,0,0],[0,0,6,-2],[0,0,0,4]] #-7, -4, 4, 6
#print(matrix_inverse_power_iteration(matrix_example,0,0.0000000000001,20000))


