'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 6 2019
written for:        Homework3 Task8
course:             Math 5610

purpose:            Implement a method that returns the product of two matrices with an equal inner dimension.
'''

def matrix_mult(vector1,vector2):
    iter_count = len(vector1[0]) # = len(vector2)
    width = len(vector2[0])
    height = len(vector1)
    final_matrix = [[0 for i in range(width)] for j in range(height)]

    for i in range(width):
        for j in range(height):
            sum = 0
            for k in range(iter_count):
                sum += vector1[j][k]*vector2[k][i]
            final_matrix[j][i] = sum

    return final_matrix


#The code below is used just for testing.
#vector1 = [[2,1,4],[0,1,1]]
#vector2 = [[6,3,-1,0],[1,1,0,4],[-2,5,0,2]]
#print(matrix_mult(vector1,vector2))
