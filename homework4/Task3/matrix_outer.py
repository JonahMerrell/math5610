'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 8 2019
written for:        Homework5 Task2
course:             Math 5610

purpose:            This method will compute the outer product of 2 vectors
'''


def matrix_outer(vector1,vector2):
    matrix_outer_product = [[0 for j in range(len(vector2))] for i in range(len(vector1))]
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            matrix_outer_product[i][j] = vector1[i] * vector2[j]

    return matrix_outer_product


#The code below is used just for testing.
#vector1 = [1,2,3,4,5]
#vector2 = [6,7,8,9,10]
#print(matrix_outer(vector1,vector2))

