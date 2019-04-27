'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 25 2019
written for:        Homework7 Task4
course:             Math 5610

purpose:            This method tests the QR factorization method on various hilbert matrices.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_conjugate_gradient, matrix_mult, matrix_transpose, abs_error_2norm, matrix_mult, convert_vec_mat

def hilbert_matrix_conjugate_gradient_test():

    selection = [4,8,16,32]
    hilbert_matrix = []
    solution = []

    # Create the hilbert matrices and their corresponding Q factorization matrix.
    for n in selection:
        hilbert_matrix.append([[1/(1+i+j) for i in range(n)] for j in range(n)])  # Hilbert Matrix generator
        solution.append(matrix_solve_conjugate_gradient(hilbert_matrix[-1],[1]*n,0.000000001,10000))

    for i in range(0,len(selection)):  # 4, 6, 8, 10
        #print(matrix_mult(hilbert_matrix[i],convert_vec_mat(solution[i])))
        print("Absolute error for " + str(selection[i]) + "x" + str(selection[i]) + ": " + str(abs_error_2norm([1]*selection[i],convert_vec_mat(matrix_mult(hilbert_matrix[i],convert_vec_mat(solution[i]))))))
        print(solution[i])
hilbert_matrix_conjugate_gradient_test()