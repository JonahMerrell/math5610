'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       March 4 2019
written for:        Homework5 Task5
course:             Math 5610

purpose:            Implement a method that performs the Cholesky factorization method for square matrices
'''
import random
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_mult, gen_sym_posdef_matrix

def matrix_cholesky_fac(matrix):
    width = len(matrix)
    L_matrix = [[0 for i in range(width)] for j in range(width)]
    for k in range(0, width):
        for i in range(0, k):
            temp_sum = matrix[k][i]
            for j in range(0, i):
                temp_sum -= L_matrix[i][j] * L_matrix[k][j]
            L_matrix[k][i] = temp_sum/L_matrix[i][i]

        temp_sum = matrix[k][k]
        for j in range(0,k):
            temp_sum -= pow(L_matrix[k][j],2)
        L_matrix[k][k] = pow(temp_sum,0.5)

    return L_matrix

#The code below is used just for testing.
#A_ = matrix_cholesky_fac(gen_sym_posdef_matrix())
#A_ = matrix_cholesky_fac([[6,15,35],[15,55,225],[55,225,979]])
#for i in range(len(A_)):
#    print(A_[i])


#[2.449489742783178, 0, 0]
#[6.123724356957946, 4.183300132670377, 0]
#[22.45365597551247, 20.916500663351886, 6.110100926607785]

#[1.2270739635610934, 0, 0, 0, 0]
#[0.9884905540342168, 0.298371883302333, 0, 0, 0]
#[0.9289152023039965, 0.4258697035898434, 0.8664237414640619, 0, 0]
#[1.0389965947620328, 0.3667018381919968, 0.5804983813458355, 0.7757989086710309, 0]
#[0.5401501093181371, 0.06033874890095169, 0.820385543390819, -0.048188040990194886, 0.08958274555125915]