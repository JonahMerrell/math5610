'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       March 12 2019
written for:        Homework5 Task1
course:             Math 5610

purpose:            This method will perform will find the solution of a matrix using a least squares technique.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_mult, matrix_solve , matrix_transpose, convert_vec_mat


def matrix_solve_least_square(matrix,vector):
    matrix_At_A = matrix_mult(matrix_transpose(matrix), matrix)
    vector_At_b = matrix_mult(matrix_transpose(matrix), convert_vec_mat(vector))
    solution = matrix_solve(matrix_At_A, convert_vec_mat(vector_At_b))
    return solution

#The code below is used just for testing.
#matrix_example = [[2,-1],[1,2],[1,1]]
#vector_example = [2,1,4]
#print(matrix_solve_least_square(matrix_example,vector_example))

