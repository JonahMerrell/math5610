'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task6
course:             Math 5610

purpose:            Calculate the 2-norm of a vector
'''
import math

def vector_2norm(vector):
    sum = 0.0
    for i in range(len(vector)):
        sum += (vector[i])*(vector[i])
    norm_2 = math.pow(sum,0.5)

    return norm_2

#The code below is used just for testing.
#vector = [5,7,9,2,5]
#print(vector_2norm(vector))

