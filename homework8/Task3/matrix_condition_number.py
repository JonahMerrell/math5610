'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task3
course:             Math 5610

purpose:            This method will approximate the condition number of a matrix by computing the largest and smallest eigenvalue.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_inverse_power_iteration, matrix_power_iteration

def matrix_condition_number(matrix):
    smallest_eigenvalue = matrix_inverse_power_iteration(matrix,0,0.00000000000001,20000)
    largest_eigenvalue = matrix_power_iteration(matrix,0.0000000001,20000)
    return abs(largest_eigenvalue/smallest_eigenvalue)

#The code below is used just for testing.
#matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
#matrix_example = [[1/(1+i+j) for i in range(6)] for j in range(6)]
#print(matrix_condition_number(matrix_example))


