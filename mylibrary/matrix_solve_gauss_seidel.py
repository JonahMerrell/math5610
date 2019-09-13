'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       April 24 2019
written for:        Homework6 Task7
course:             Math 5610

purpose:            This method will find the solution of a matrix using the gauss seidel iteration
'''

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_scal_mult,vector_add, vector_2norm, matrix_mult, convert_vec_mat

def matrix_solve_gauss_seidel(matrix,vector_b,tol,max_iter,getIterCount=False):
    xnew = [0 for i in range(len(matrix))]
    error = tol * 10
    count = 0
    while error > tol and count < max_iter:
        #print(count) used for testing
        #print(error) used for testing
        count +=1
        xold = xnew.copy()
        xnew = vector_b.copy()
        for i in range(len(matrix)):
            for j in range(i):
                xnew[i] = xnew[i] - matrix[i][j]*xold[j]
            for j in range(i+1,len(xnew)):
                xnew[i] = xnew[i] - matrix[i][j]*xold[j]
            xnew[i] = xnew[i] / matrix[i][i]
            xold[i] = xnew[i]
        error = vector_2norm(vector_add(convert_vec_mat(matrix_mult(matrix,convert_vec_mat(xnew))),vector_scal_mult(-1,vector_b)))
    if getIterCount == True:
        return xnew,count
    else:
        return xnew

#The code below is used just for testing.
#matrix_example = [[5,1,2],[1,4,1],[2,2,5]]
#vector_example = [1,2,3]
#print(matrix_solve_gauss_seidel(matrix_example,vector_example,0.00001,40))


