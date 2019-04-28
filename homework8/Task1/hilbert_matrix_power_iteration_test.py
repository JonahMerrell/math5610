import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import matrix_power_iteration, matrix_mult, matrix_transpose, abs_error_2norm, matrix_mult, convert_vec_mat

def hilbert_matrix_power_iteration_test():

    selection = [4,6,8,10]
    hilbert_matrix = []
    solution = []

    # Create the hilbert matrices and their corresponding Q factorization matrix.
    for n in selection:
        hilbert_matrix.append([[1/(1+i+j) for i in range(n)] for j in range(n)])  # Hilbert Matrix generator
        solution.append(matrix_power_iteration(hilbert_matrix[-1],0.000000001,10000))

    for i in range(0,len(selection)):  # 4, 6, 8, 10
        #print(matrix_mult(hilbert_matrix[i],convert_vec_mat(solution[i])))
        print("Largest Eigen Value for " + str(selection[i]) + "x" + str(selection[i]) + ": " + str(solution[i]))

hilbert_matrix_power_iteration_test()