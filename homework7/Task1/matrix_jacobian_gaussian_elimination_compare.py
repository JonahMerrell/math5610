'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 25 2019
written for:        Homework7 Task1
course:             Math 5610

purpose:            This method compares the Jacobian iteration and Gaussian elimination in terms of the computational time needed.
'''
import random
import sys, os
import time

sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve, matrix_solve_jacobian, gen_sqr_diagdom_matrix


def matrix_jacobian_gaussian_elimination_compare():
    for i in [10,50,100,200,500]:
        matrix = gen_sqr_diagdom_matrix(i)
        vector = [1]*i
        starttime = time.time()
        solution,count = matrix_solve_jacobian(matrix, vector, 0.0001, 10000,getIterCount=True)
        print(str(i)+ "x" + str(i) + " Jacobian:             Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))
        starttime = time.time()
        solution = matrix_solve(matrix, vector)
        print(str(i)+ "x" + str(i) + " Gaussian elimination: Time: " + str(time.time() - starttime))

matrix_jacobian_gaussian_elimination_compare()
