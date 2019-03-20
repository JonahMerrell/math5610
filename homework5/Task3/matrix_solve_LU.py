'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 20 2019
written for:        Homework4 Task7
course:             Math 5610

purpose:            This method will perform elementary row operations on a matrix to take the matrix to row echelon form
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
#output: [1.0, 2.0, -1.0]

