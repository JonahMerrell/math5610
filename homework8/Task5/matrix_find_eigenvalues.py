'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task5
course:             Math 5610

purpose:            This method will find the various eigenvalues of a matrix by computing the smallest and largest
                    eigenvalues, and then subdividing the region inbetween to find additional eigenvalues.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_inverse_power_iteration, matrix_power_iteration

def matrix_find_eigenvalues(matrix):
    eigenvalues = []
    eigenvalues.append(matrix_inverse_power_iteration(matrix,0.56,0.00000000000001,20000))
    eigenvalues.append(matrix_power_iteration(matrix,0.0000000001,20000))
    find_middle_eigenvalue(matrix,eigenvalues,eigenvalues[0],eigenvalues[1])
    return eigenvalues

def find_middle_eigenvalue(matrix,eigenvalues,min_value,max_value):
    middle = (max_value + min_value) / 2
    middle_eigenvalue, count = matrix_inverse_power_iteration(matrix, middle, 0.00000000000001, 1000,getIterCount=True)
    if (count != 1000):#If no convergence happens after 1000 iterations, then middle is probably right inbetween the only 2 eigenvalues.
        if (not abs(middle_eigenvalue - min_value) < 0.0001) and (not abs(middle_eigenvalue - max_value) < 0.0001):
            eigenvalues.append(middle_eigenvalue)
            find_middle_eigenvalue(matrix, eigenvalues, min_value, middle_eigenvalue)
            find_middle_eigenvalue(matrix, eigenvalues, middle_eigenvalue, max_value)


#The code below is used just for testing.
#matrix_example = [[-16,9,0,0],[-12,5,0,0],[0,0,6,-2],[0,0,0,4]] #-7, -4, 4, 6
#matrix_example = [[7,1,1],[3,1,2],[1,3,2]]
#print(matrix_find_eigenvalues(matrix_example))


