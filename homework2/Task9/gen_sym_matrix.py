'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 12 2019
written for:        Homework1 Task9
course:             Math 5610

purpose:            Create a n*n matrix (the size is inputted from the user) with random entries from 0 to 1.
'''
import numpy as np
import random

def generate_sym_matrix():
    width = int(input("Please enter the width of the square matrix: "))
    A = np.array([[0]],dtype=float)
    A.resize((width,width))
    for i in range(0,width):
        for j in range(i, width):
            value = random.random()
            A[j,i] = value
            A[i,j] = value
    return A

#The code below is used just for testing.
print(generate_sym_matrix())


