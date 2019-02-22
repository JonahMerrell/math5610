'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 20 2019
written for:        Homework4 Task7
course:             Math 5610

purpose:            This method will perform elementary row operations on a matrix to take the matrix to row echelon form
'''
import copy
import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_add, vector_scal_mult



def matrix_ref(matrix):
    n = len(matrix)
    #m = len(matrix[0])
    solution = copy.deepcopy(matrix)
    for i in range(0,n):
        for j in range(i+1, n):
            if solution[i][i] !=0:
                solution[j] = vector_add(solution[j],vector_scal_mult(-solution[j][i]/solution[i][i],solution[i]))
        solution[i] = vector_scal_mult(1/solution[i][i],solution[i])
    return solution


#The code below is used just for testing.
#matrix = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
#matrix_new = matrix_ref(matrix)
#for i in range(0,len(matrix)):
#    print(matrix_new[i])
