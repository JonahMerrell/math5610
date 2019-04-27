'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 26 2019
written for:        Homework7 Task10
course:             Math 5610

purpose:            This method will find the solution of a matrix using the jacobian iteration. This particular
                    algorithm will modify the original matrix so that it is diagnal dominant (which garintees that
                    the jacobian iteration will converge). This method also transforms the matrix to be normal equations.
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_scal_mult, vector_add, vector_2norm, matrix_mult, convert_vec_mat,matrix_transpose

def matrix_solve_jacobian_smart(matrix,vector_b,tol,max_iter,getIterCount=False):
    matrix_mod = matrix_mult(matrix_transpose(matrix),matrix)
    vector_mod = convert_vec_mat(matrix_mult(matrix_transpose(matrix),convert_vec_mat(vector_b)))
    alpha = 0
    #This code finds the right valu for alpha to garintee that matrix_mod is diagonoly dominant.
    for i in range(len(matrix_mod)):
        tempVal = 0
        for j in range(len(matrix_mod[0])):
            if j != i:
                tempVal += matrix_mod[i][j]
            else:
                tempVal -= matrix_mod[i][j]
        alpha = max(alpha,tempVal)
    xnew = [0 for i in range(len(matrix_mod))]
    error = tol * 10
    count = 0
    while error > tol and count < max_iter:
        count += 1
        xold = xnew.copy()
        xnew = [(vector_mod[i]+alpha*xold[i]) for i in range(len(xold))]
        for i in range(len(matrix_mod)):
            for j in range(i):
                xnew[i] = xnew[i] - matrix_mod[i][j] * xold[j]
            for j in range(i + 1, len(xnew)):
                xnew[i] = xnew[i] - matrix_mod[i][j] * xold[j]
        for j in range(len(xnew)):
            xnew[j] = xnew[j] / (matrix_mod[j][j] + alpha)

        error = vector_2norm(vector_add(convert_vec_mat(matrix_mult(matrix, convert_vec_mat(xnew))), vector_scal_mult(-1, vector_b)))
    if getIterCount == True:
        return xnew,count
    else:
        return xnew

# The code below is used just for testing.
#matrix_example = [[5,10,2],[1,4,10],[2,1,5]]
#vector_example = [1,2,3]
#print(matrix_solve_jacobian_smart(matrix_example,vector_example,0.00001,10000))


