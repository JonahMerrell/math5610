'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 20 2019
written for:        Homework4 Task7
course:             Math 5610

purpose:            This method will compute the solution of a square linear system of equations where the coefficient matrix is lower triangular.
'''

def matrix_solve_lower_tri(matrix,vector):
    n = len(matrix)
    solution = [0]*len(vector)

    for i in range(0, n, 1):
        temp_var = vector[i]
        for j in range(i, -1, -1):
            temp_var -= matrix[i][j] * solution[j]
        solution[i] = temp_var/matrix[i][i]

    return solution




#The code below is used just for testing.
#matrix = [[8,0,0,0,0],[1,3,0,0,0],[3,7,2,0,0],[2,7,5,2,0],[7,3,10,8,4]]
#vector = [12,25,38,27,48]
matrix = [[1,0,0],[1,1,0],[2,-0.3333333333333333,1]]
vector = [4,-6,7]
print(matrix_solve_lower_tri(matrix,vector))
