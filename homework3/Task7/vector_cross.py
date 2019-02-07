'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 6 2019
written for:        Homework3 Task7
course:             Math 5610

purpose:            Implement a method that returns the cross-product of two vectors of length three.
'''

def vector_dot(vector1,vector2):
    vector_dotted = [0,0,0]
    vector_dotted[0] = vector1[1]*vector2[2] - vector1[2]*vector2[1]
    vector_dotted[1] = vector1[2] * vector2[0] - vector1[0] * vector2[2]
    vector_dotted[2] = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    return vector_dotted


#The code below is used just for testing.
#vector1 = [5,7,9]
#vector2 = [8,2,3]
#print(vector_dot(vector1,vector2))

