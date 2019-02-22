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
from _mymodules import matrix_ref, matrix_solve_upper_tri


def matrix_solve(matrix,vector):
    n = len(matrix)
    solution = [0] * len(vector)
    for i in range(n):
        matrix[i].append(vector[i])
    ref_matrix = matrix_ref(matrix)
    for i in range(n):
        solution[i] = ref_matrix[i][-1]
        del ref_matrix[i][-1]

    solution = matrix_solve_upper_tri(ref_matrix,solution)

    return solution




#The code below is used just for testing.
#matrix_example = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
#vector_example = [12,25,38,27,48]
#print(matrix_solve(matrix_example,vector_example))



