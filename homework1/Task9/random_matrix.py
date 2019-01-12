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
    print(A)


generate_random_matrix()


