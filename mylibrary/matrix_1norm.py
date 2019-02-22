'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 19 2019
written for:        Homework3 Task4
course:             Math 5610

purpose:            Implement a method that returns the 1-matrix norm of a given square matrix.
'''

def matrix_1norm(matrix):
    temp_list = []
    for j in range(len(matrix[0])):
        sum = 0.0
        for i in range(len(matrix)):
            sum += abs(matrix[i][j])
        temp_list.append(sum)

    return max(temp_list)

#The code below is used just for testing.
#matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#print(matrix_1norm(matrix))

