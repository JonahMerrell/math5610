import time
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_solve_least_square, matrix_solve, gen_rand_matrix

def normal_equations_speed_test():

test_matrix = gen_rand_matrix()
test_vector = gen_rand_matrix()
test_vector = [test_vector[i][0] for i in range(len(test_vector))]

start_time = time.time()
matrix_solve_least_square(test_matrix,test_vector)
end_time = time.time() - start_time
print(end_time)

start_time = time.time()
matrix_solve(test_matrix,test_vector)
end_time = time.time() - start_time
print(end_time)

'''
Please enter the width of the matrix: 300
Please enter the height of the matrix: 300
Please enter the width of the matrix: 1
Please enter the height of the matrix: 300
12.222699403762817
5.036288022994995
'''
