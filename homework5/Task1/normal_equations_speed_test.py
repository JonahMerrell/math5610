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
    print("Least Squares method: " + str(end_time))

    start_time = time.time()
    matrix_solve(test_matrix,test_vector)
    end_time = time.time() - start_time
    print("Guassian elimination method: " + str(end_time))

normal_equations_speed_test()

'''
Please enter the width of the matrix: 400
Please enter the height of the matrix: 400
Please enter the width of the matrix: 1
Please enter the height of the matrix: 400
Least Squares method: 29.101664543151855
Guassian elimination method: 12.16169548034668

Please enter the width of the matrix: 300
Please enter the height of the matrix: 300
Please enter the width of the matrix: 1
Please enter the height of the matrix: 300
Least Squares method: 12.057689666748047
Guassian elimination method: 5.129293441772461

Please enter the width of the matrix: 100
Please enter the height of the matrix: 100
Please enter the width of the matrix: 1
Please enter the height of the matrix: 100
Least Squares method: 0.4370250701904297
Guassian elimination method: 0.18301057815551758

'''
