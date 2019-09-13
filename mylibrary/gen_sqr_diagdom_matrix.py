'''
coding language:    Python 3.7.0
written by:         Jonah Merrell
date written:       March 22 2019
written for:        Homework5 Task9
course:             Math 5610
purpose:            Implement a method that will generate a square diagonally dominant matrix.
'''
import random

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_1norm

def gen_sqr_diagdom_matrix(width=0):
    if width == 0:
        width = int(input("Please enter the width of the square matrix: "))

    A = [[0 for i in range(width)] for j in range(width)]
    for i in range(0, width):
        for j in range(0, width):
            value = random.random()
            A[j][i] = value

    for i in range(0, width):
        value = vector_1norm(A[i])
        A[i][i] = value
    return A

#The code below is used just for testing.
A_ = gen_sqr_diagdom_matrix(6)
for i in range(len(A_)):
    print(A_[i])