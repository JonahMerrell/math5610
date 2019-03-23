'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       March 22 2019
written for:        Homework5 Task8
course:             Math 5610

purpose:            This method tests the QR factorization method on various hilbert matrices.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_QR_factorization, matrix_mult, matrix_transpose

def hilbert_matrix_QR_test():


    hilbert_matrix = [0]*11
    Q_matrix = [0]*11

    # Create the hilbert matrices and their corresponding Q factorization matrix.
    for n in range(1,11):
        hilbert_matrix[n] = [[1/(1+i+j) for i in range(n)] for j in range(n)]  # Hilbert Matrix generator
        Q_matrix[n] = matrix_QR_factorization(hilbert_matrix[n])[0]

    # Print the Q-factorized hilbert matrix, as well as Q^t*Q
    for i in range(4,11,2):  # 4, 6, 8, 10
        print("Given a " + str(i) + "-sized Hilbert matrix, its Q matrix is:")
        for j in range(i):
            print(Q_matrix[i][j])

        print("Q^t*Q should result in the identity matrix:")
        temp_matrix = matrix_mult(Q_matrix[i],matrix_transpose(Q_matrix[i]))
        for j in range(i):
            print(temp_matrix[j])

        print()  # Print a new line for organization purposes.

#hilbert_matrix_QR_test()