'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 8 2019
written for:        Homework4 Task4
course:             Math 5610

purpose:            This method will compute the solution of a square linear system of equations where the coefficient matrix is a diagonal matrix.
'''

def matrix_solve_diagonal(matrix,vector):
    width = len(matrix)
    solution = [0]*len(vector)

    for i in range(width):
        solution[i] = vector[i]/matrix[i][i]

    return solution


#The code below is used just for testing.
#matrix = [[4,0,0,0,0],[0,5,0,0,0],[0,0,2,0,0],[0,0,0,3,0],[0,0,0,0,8]]
#vector = [12,25,38,27,48]
#print(matrix_solve_diagonal(matrix,vector))
