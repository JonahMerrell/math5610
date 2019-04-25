'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 12 2019
written for:        Homework6 Task6
course:             Math 5610

purpose:            This method will find the solution of a matrix using QR factorization and back substitution
'''
import random
import sys, os
import time
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_gauss_seidel, matrix_solve_jacobian, gen_sqr_diagdom_matrix


def matrix_jacobian_gauss_seidel_compare():
    #for i in [10,50,100,200,500]:
    for i in [1000]:
        matrix = gen_sqr_diagdom_matrix(i)
        vector = [1]*i
        starttime = time.time()
        solution,count = matrix_solve_jacobian(matrix, vector, 0.0001, 10000,getIterCount=True)
        print(str(i)+ "x" + str(i) + " Jacobian:     Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))
        starttime = time.time()
        solution, count = matrix_solve_gauss_seidel(matrix, vector, 0.0001, 10000,getIterCount=True)
        print(str(i)+ "x" + str(i) + " Gauss Seidel: Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))

matrix_jacobian_gauss_seidel_compare()
