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
from _mymodules import gen_sqr_diagdom_matrix, matrix_mult, convert_vec_mat
from matrix_solve_gauss_seidel import matrix_solve_gauss_seidel

def matrix_solve_gauss_seidel_test():
    matrix = gen_sqr_diagdom_matrix()
    vector = [1]*len(matrix)
    print("created matrix")
    starttime = time.time()

    solution = matrix_solve_gauss_seidel(matrix, vector, 0.001, 10000)

    print("Time: " + str(time.time() - starttime))
    print(matrix_mult(matrix,convert_vec_mat(solution)))

matrix_solve_gauss_seidel_test()
