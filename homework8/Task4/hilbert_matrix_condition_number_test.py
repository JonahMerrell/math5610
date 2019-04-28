'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task4
course:             Math 5610

purpose:            This method tests the condition number for various-sized hilbert matrices
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_condition_number

def hilbert_matrix_condition_number_test():

    selection = [4,6,8,10]
    hilbert_matrix = []
    solution = []

    # Create the hilbert matrices and their corresponding Q factorization matrix.
    for n in selection:
        hilbert_matrix.append([[1/(1+i+j) for i in range(n)] for j in range(n)])  # Hilbert Matrix generator
        solution.append(matrix_condition_number(hilbert_matrix[-1]))

    for i in range(0,len(selection)):  # 4, 6, 8, 10
        #print(matrix_mult(hilbert_matrix[i],convert_vec_mat(solution[i])))
        print("Condition number for " + str(selection[i]) + "x" + str(selection[i]) + ": " + str(solution[i]))

hilbert_matrix_condition_number_test()