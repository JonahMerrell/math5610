'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 8 2019
written for:        Homework5 Task2
course:             Math 5610

purpose:            This method will return the sum of two matrices of the same size.
'''


def matrix_add(matrix1,matrix2):
    matrix_sum = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]
    for i in range(len(matrix_sum)):
        for j in range(len(matrix_sum[0])):
            matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j]

    return matrix_sum


#The code below is used just for testing.
#matrix1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#matrix2 = [[26,27,28,29,30],[31,32,33,34,35],[36,37,38,39,40],[41,42,43,44,45],[46,47,48,49,50]]
#print(matrix_add(matrix1,matrix2))

