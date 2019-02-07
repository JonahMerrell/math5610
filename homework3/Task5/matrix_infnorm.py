'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 19 2019
written for:        Homework3 Task5
course:             Math 5610

purpose:            Implement a method that returns the infinity-matrix norm of a given square matrix.
'''

def matrix_infnorm(matrix):
    maximum = 0.0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
    return maximum

#The code below is used just for testing.
#matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#print(matrix_infnorm(matrix))

