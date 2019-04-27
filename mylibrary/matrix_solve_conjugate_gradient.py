'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 12 2019
written for:        Homework6 Task4
course:             Math 5610

purpose:            This method will find the solution of a matrix using QR factorization (modified gram schmidt) and back substitution
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_add, vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, vector_dot


def matrix_solve_conjugate_gradient(matrix,vector_b,tol,max_iter,getIterCount=False):
    error = tol * 10
    count = 0
    x_i = vector_b.copy()  # x_0
    residual = vector_add(vector_b, vector_scal_mult(-1, convert_vec_mat(matrix_mult(matrix, convert_vec_mat(x_i)))))
    direction = residual
    d1new = vector_dot(residual, residual)

    while error > tol and count < max_iter:
        s = convert_vec_mat(matrix_mult(matrix,convert_vec_mat(direction)))
        d1old = d1new
        alpha = d1old / vector_dot(direction, s)
        x_i = vector_add(x_i,vector_scal_mult(alpha,direction))
        residual = vector_add(residual,vector_scal_mult(-alpha, s))
        d1new = vector_dot(residual, residual)
        direction = vector_add(residual,vector_scal_mult(d1new/d1old,direction))
        count += 1
        error = vector_2norm(residual)
    if getIterCount == True:
        return x_i, count
    else:
        return x_i

#The code below is used just for testing.
#matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
#vector_example = [1, 2, 3]
#print(matrix_solve_conjugate_gradient(matrix_example,vector_example,0.00001,1000))


