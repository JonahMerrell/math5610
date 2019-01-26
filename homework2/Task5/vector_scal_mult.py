'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task5
course:             Math 5610

purpose:            Multiply the given vector by a scalar.
'''


def vector_scal_mult(scalar,vector):
    for i in range(len(vector)):
        vector[i] *= scalar

    return vector

#The code below is used just for testing.
#vector = [5,7,9,2,5]
#print(vector_scal_mult(5,vector))

