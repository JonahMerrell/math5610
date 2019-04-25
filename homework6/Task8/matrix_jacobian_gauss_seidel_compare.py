'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 24 2019
written for:        Homework6 Task8
course:             Math 5610

purpose:            This method compares the Jacobian and Gauss-Seidel iterations in terms of the number of iterations needed to converge to a given tolerance.
'''
import random
import sys, os
import time

sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_gauss_seidel, matrix_solve_jacobian, gen_sqr_diagdom_matrix


def matrix_jacobian_gauss_seidel_compare():
    for i in [10,50,100,200,500]:
        matrix = gen_sqr_diagdom_matrix(i)
        vector = [1]*i
        starttime = time.time()
        solution,count = matrix_solve_jacobian(matrix, vector, 0.0001, 10000,getIterCount=True)
        print(str(i)+ "x" + str(i) + " Jacobian:     Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))
        starttime = time.time()
        solution, count = matrix_solve_gauss_seidel(matrix, vector, 0.0001, 10000,getIterCount=True)
        print(str(i)+ "x" + str(i) + " Gauss Seidel: Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))

matrix_jacobian_gauss_seidel_compare()
