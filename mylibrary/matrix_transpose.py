
def matrix_transpose(matrix):
    #width = len(matrix[0])
    #height = len(matrix)
    #solution_matrix = [[0 for i in range(height)] for j in range(width)]
    #for i in range(len(matrix)):
    #    for j in range(len(matrix[0])):
    #        solution_matrix[j][i] = matrix[i][j]
    #return solution_matrix
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
