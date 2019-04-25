'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 11 2019
written for:        Homework6 Task2
course:             Math 5610

purpose:            This method will Implement the QR factorization of a square matrix using the modified gram schmidt algorithm
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_dot, vector_scal_mult, vector_add, vector_2norm, matrix_mult, matrix_transpose

def matrix_QR_factorization_mod(matrix):

    u_vectors = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for j in range(len(matrix[0])):
        for i in range(j):
            u_vectors[j] = vector_add(u_vectors[j],vector_scal_mult(-1 * vector_dot(u_vectors[j], u_vectors[i]), u_vectors[i]))
        u_vectors[j] = vector_scal_mult(1 / vector_2norm(u_vectors[j]), u_vectors[j])

    matrix_Q = [[u_vectors[i][j] for i in range(len(u_vectors))] for j in range(len(u_vectors[0]))]
    matrix_R = matrix_mult(matrix_transpose(matrix_Q), matrix)

    return [matrix_Q,matrix_R]

#The code below is used just for testing.
#matrix_example = [[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]]
#matrix_new = matrix_QR_factorization_mod(matrix_example)
#for i in range(0,len(matrix_new[0])):
#    print(matrix_new[0][i])
#for i in range(0,len(matrix_new[1])):
#    print(matrix_new[1][i])
#print(matrix_mult(matrix_new[0],matrix_new[1]))
