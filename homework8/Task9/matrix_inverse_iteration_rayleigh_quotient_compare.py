'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 27 2019
written for:        Homework8 Task9
course:             Math 5610

purpose:            This method compares the Jacobian iteration and Gaussian elimination in terms of the computational time needed.
'''
import random
import sys, os
import time

sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_rayleigh_quotient_iteration, matrix_inverse_power_iteration, gen_sqr_diagdom_matrix

def matrix_inverse_iteration_rayleigh_quotient_compare():
    for i in [10,50,100,200]:
        matrix = gen_sqr_diagdom_matrix(i)
        #vector = [1]*i
        starttime = time.time()
        solution, count = matrix_inverse_power_iteration(matrix,0, 0.0001, 10000, getIterCount=True)
        print(str(i)+ "x" + str(i) + " Inverse_Power: Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))
        starttime = time.time()
        solution, count = matrix_rayleigh_quotient_iteration(matrix, 0.0001, 10000, getIterCount=True)
        print(str(i)+ "x" + str(i) + " Rayleigh Quotient: Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))

matrix_inverse_iteration_rayleigh_quotient_compare()
