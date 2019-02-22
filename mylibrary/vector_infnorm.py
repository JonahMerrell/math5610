'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task8
course:             Math 5610

purpose:            Calculate the infinity-norm of a vector
'''

def vector_infnorm(vector):
    temp_max = 0
    for i in range(len(vector)):
        if temp_max < abs(vector[i]):
            temp_max = abs(vector[i])
    return temp_max

#The code below is used just for testing.
#vector = [5,7,9,2,5]
#print(vector_infnorm(vector))

