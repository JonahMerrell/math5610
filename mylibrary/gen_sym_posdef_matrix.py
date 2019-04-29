'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       Match 4 2019
written for:        Homework5 Task4
course:             Math 5610

purpose:            Implement a method that will generate a symmetric, positive definite matrix.
'''
import random

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_mult

def gen_sym_posdef_matrix(width=0):
    if width == 0:
        width = int(input("Please enter the width of the symmetric, positive definite matrix: "))
    A = [[0 for i in range(width)] for j in range(width)]
    for i in range(0, width):
        for j in range(0, width):
            value = random.random()
            A[j][i] = value
    B = [[0 for i in range(width)] for j in range(width)]
    for i in range(0, width):
        for j in range(0, width):
            B[j][i] = A[i][j]

    return matrix_mult(A,B)

#The code below is used just for testing.
#A_ = gen_sym_posdef_matrix()
#for i in range(len(A_)):
#    print(A_[i])

#[2.1299916128935443, 1.6552058122613746, 1.0669733563946053, 2.303370684810509, 2.1555965022580246]
#[1.6552058122613746, 1.7714872334525005, 1.0557926024679505, 1.9943425085828212, 1.7498183443173871]
#[1.0669733563946053, 1.0557926024679505, 1.221063943602681, 1.7310340736520864, 1.4262247484195203]
#[2.303370684810509, 1.9943425085828212, 1.7310340736520864, 3.2903144257120633, 2.5746650478275868]
#[2.1555965022580246, 1.7498183443173871, 1.4262247484195203, 2.5746650478275868, 2.3716161253944574]
