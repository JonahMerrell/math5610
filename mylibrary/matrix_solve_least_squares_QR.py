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
from _mymodules import matrix_QR_factorization_mod, matrix_solve_upper_tri, matrix_mult, matrix_transpose, convert_vec_mat


def matrix_solve_least_squares_QR(matrix,vector):
    (matrix_Q, matrix_R) = matrix_QR_factorization_mod(matrix)
    matrix_Qtb = matrix_mult(matrix_transpose(matrix_Q), convert_vec_mat(vector))
    solution = matrix_solve_upper_tri(matrix_R, convert_vec_mat(matrix_Qtb))
    return solution

#The code below is used just for testing.
#matrix_example = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
#vector_example = [12,25,38,27,48]
#print(matrix_solve_least_squares_QR(matrix_example,vector_example))


