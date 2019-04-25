import random
import sys, os
import time
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import gen_sqr_diagdom_matrix, matrix_mult, convert_vec_mat
from matrix_solve_jacobian import matrix_solve_jacobian

def matrix_solve_jacobian_test():
    matrix = gen_sqr_diagdom_matrix()
    vector = [1] * len(matrix)
    print("created matrix")
    starttime = time.time()

    solution = matrix_solve_jacobian(matrix, vector, 0.001, 10000)

    print("Time: " + str(time.time() - starttime))
    print(matrix_mult(matrix, convert_vec_mat(solution)))

matrix_solve_jacobian_test()
