'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       March 12 2019
written for:        Homework5 Task6
course:             Math 5610

purpose:            This method will find the solution of a matrix using the least squares technique with normal equations.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_mult , matrix_transpose, matrix_cholesky_fac, matrix_solve_lower_tri, matrix_solve_upper_tri


def matrix_solve_least_square_normal(matrix,vector):
    vector = [[vector[i]] for i in range(len(vector))]
    matrix_A_At = matrix_mult(matrix_transpose(matrix),matrix)
    vector_At_b = matrix_mult(matrix_transpose(matrix),vector)
    matrix_G = matrix_cholesky_fac(matrix_A_At)
    vector_y = matrix_solve_lower_tri(matrix_G,matrix_transpose(vector_At_b)[0])
    vector_x = matrix_solve_upper_tri(matrix_transpose(matrix_G),vector_y)
    return vector_x

#The code below is used just for testing.
#matrix_example = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
#vector_example = [12,25,38,27,48]
#print(matrix_solve_least_square_normal(matrix_example,vector_example))

#[2.6226777706598434, -1.3299167200512514, -1.725816784112757, -1.1672005124920306, 6.659192825112138]


