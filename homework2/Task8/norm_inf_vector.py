'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task8
course:             Math 5610

purpose:            Calculate the infinity-norm of a vector
'''
import numpy as np

def norm_inf_vector(vector):
    norm_inf = max(vector[0])
    #for i in range(len(vector[0])):
    #    sum += vector[0,i]

    return norm_inf

#The code below is used just for testing.
#vector = np.array([[5,7,9,2,5]] , dtype=float)
#print(norm_inf_vector(vector))

