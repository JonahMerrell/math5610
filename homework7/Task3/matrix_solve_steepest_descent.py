'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 24 2019
written for:        Homework7 Task3
course:             Math 5610

purpose:            This method will solve the system of equations using the steepest descent method.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_add, vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, vector_dot


def matrix_solve_steepest_descent(matrix,vector_b,tol,max_iter):
    error = tol * 10
    count = 0
    x_i = vector_b.copy() #x_0
    while error > tol and count < max_iter:
        #print(count)# used for testing
        #print(error)# used for testing
        count += 1
        residual = vector_add(vector_b,vector_scal_mult(-1, convert_vec_mat(matrix_mult(matrix, convert_vec_mat(x_i)))))
        d1 = vector_dot(residual,residual)
        d2 = vector_dot(residual, convert_vec_mat(matrix_mult(matrix,convert_vec_mat(residual))))
        alpha = d1/d2
        x_i = vector_add(x_i, vector_scal_mult(alpha, residual))
        error = vector_2norm(residual)
    return x_i


# The code below is used just for testing.
#matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
#vector_example = [1, 2, 3]
#print(matrix_solve_steepest_descent(matrix_example, vector_example, 0.00001, 40))


