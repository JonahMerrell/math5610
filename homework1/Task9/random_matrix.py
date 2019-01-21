'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 12 2019
written for:        Homework1 Task9
course:             Math 5610

purpose:            Create a n*m matrix (the size is inputted from the user) with random entries from 0 to 1.
'''
import numpy as np
import random

def generate_random_matrix():
    width = int(input("Please enter the width of the matrix: "))
    height = int(input("Please enter the height of the matrix: "))
    A = np.array([[0]],dtype=float)
    A.resize((height,width))
    for i in range(0,width):
        for j in range(0, height):
            A[j,i] = random.random()
    return A

#The code below is used just for testing.
#print(generate_random_matrix())


