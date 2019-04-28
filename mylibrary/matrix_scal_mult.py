'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 8 2019
written for:        Homework4 Task1
course:             Math 5610

purpose:            This method will multiply the given Matrix by a scalar.
'''

def matrix_scal_mult(scalar,matrix):
    matrix_new = [[scalar*matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))]

    return matrix_new

#The code below is used just for testing.
#matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#print(matrix_scal_mult(5,matrix))

