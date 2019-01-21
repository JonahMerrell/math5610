'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task4
course:             Math 5610

purpose:            Add the components of 2 equal size vectors together.
'''
import numpy as np



def add_vectors(vector1,vector2):
    vector3 = np.array([[0]* len(vector1[0])] , dtype=float)
    for i in range(len(vector1[0])):
        vector3[0,i] = vector1[0,i] + vector2[0,i]

    return vector3


#The code below is used just for testing.
#vector1 = np.array([[5,7,9,2,5]] , dtype=float)
#vector2 = np.array([[8,2,3,6,9]] , dtype=float)
#print(add_vectors(vector1,vector2))

