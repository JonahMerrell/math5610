'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task7
course:             Math 5610

purpose:            Calculate the 1-norm of a vector
'''
import numpy as np

def norm_2_vector(vector):
    sum = np.float64(0.0)
    for i in range(len(vector[0])):
        sum += vector[0,i]

    return sum

#The code below is used just for testing.
#vector = np.array([[5,7,9,2,5]] , dtype=float)
#print(norm_2_vector(vector))

