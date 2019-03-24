'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       March 12 2019
written for:        Homework5 Task3
course:             Math 5610

purpose:            This method will solve a system of linear equations by performing LU factorization, followed with forward substitution and back substitution.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_upper_tri, matrix_solve_lower_tri,matrix_LU_factor


def matrix_solve_LU(matrix,vector):
    temp_list = matrix_LU_factor(matrix)
    matrix_l = temp_list[0]
    matrix_u = temp_list[1]
    solution_y = matrix_solve_lower_tri(matrix_l,vector)
    solution_x = matrix_solve_upper_tri(matrix_u,solution_y)
    return solution_x

#The code below is used just for testing.
#matrix_example = [[1,1,-1],[1,-2,3],[2,3,1]]
#vector_example = [4,-6,7]
#print(matrix_solve_LU(matrix_example,vector_example))


