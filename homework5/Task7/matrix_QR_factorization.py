'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       March 21 2019
written for:        Homework5 Task7
course:             Math 5610

purpose:            This method will find the solution of a matrix using a least squares technique with QR factorization.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_dot, vector_scal_mult, vector_add, vector_2norm, matrix_mult, matrix_transpose

def matrix_QR_factorization(matrix):

    matrix_columns = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    u_vectors = []
    for i in range(len(matrix[0])):
        u_vectors.append(matrix_columns[i])
        for j in range(i):
            u_vectors[i] = vector_add(u_vectors[i],vector_scal_mult(-1*vector_dot(matrix_columns[i],u_vectors[j]),u_vectors[j]))
        u_vectors[i] = vector_scal_mult(1/vector_2norm(u_vectors[i]),u_vectors[i])

    matrix_Q = [[u_vectors[i][j] for i in range(len(u_vectors))] for j in range(len(u_vectors[0]))]
    matrix_R = matrix_mult(matrix_transpose(matrix_Q),matrix)

    return [matrix_Q,matrix_R]

#The code below is used just for testing.
#matrix_example = [[1,2,4],[0,0,5],[0,3,6]]
#matrix_new = matrix_QR_factorization(matrix_example)
#for i in range(0,len(matrix_example)):
#    print(matrix_new[0][i])
#for i in range(0,len(matrix_example)):
#    print(matrix_new[1][i])


