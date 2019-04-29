'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task6
course:             Math 5610

purpose:            This method will find an eigenvector of a matrix using the rayleigh quotient iteration.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_scal_mult, vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose, matrix_solve_LU, matrix_add


def matrix_rayleigh_quotient_iteration(matrix,tol,max_iter,getIterCount=False):
    error = tol * 10
    count = 0
    v_i = matrix[0]
    v_i = vector_scal_mult(1 / vector_2norm(v_i), v_i)
    eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)), matrix_mult(matrix, convert_vec_mat(v_i)))[0][0]
    I = [[int(i == j) for i in range(len(matrix))] for j in range(len(matrix))]

    while error > tol and count < max_iter:
        eigenvalueold = eigenvaluenew
        v_i = matrix_solve_LU(matrix_add(matrix,matrix_scal_mult(-eigenvaluenew,I)),v_i)
        v_i = vector_scal_mult(1/vector_2norm(v_i),v_i)
        eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)), matrix_mult(matrix, convert_vec_mat(v_i)))[0][0]
        error = abs(eigenvaluenew - eigenvalueold)
        count += 1
    if getIterCount == True:
        return eigenvaluenew,count
    else:
        return eigenvaluenew


#The code below is used just for testing.
#matrix_example = [[-16,9,0,0],[-12,5,0,0],[0,0,6,-2],[0,0,0,4]] #-7, -4, 4, 6
#matrix_example = [[1/(1+i+j) for i in range(4)] for j in range(4)]
#print(matrix_rayleigh_quotient_iteration(matrix_example,0.0000000000001,20000))


