'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task5
course:             Math 5610

purpose:            Multiply the given vector by a scalar.
'''
import numpy as np

def add_vectors(scalar,vector):
    for i in range(len(vector[0])):
        vector[0,i] *= scalar

    return vector

#The code below is used just for testing.
#vector = np.array([[5,7,9,2,5]] , dtype=float)
#print(add_vectors(5,vector))

