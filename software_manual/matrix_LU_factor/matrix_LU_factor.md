# Software Manual (matrix_LU_factor.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_LU_factor.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine return the LU-factorization of a square matrix A. The 2 matrices L and U returned from this routine satisfy LU = A (Where A is the original matrix, and L is a lower triangle matrix, and U is an upper triangle matrix).

**Input:** argument1: The matrix to perform LU factorization on<br>
		   
**Output:** This routine returns a list containing 2 elements. The first element is the
 lower triangle matrix, and the second element is the upper triangle matrix.

**Usage/Example:**

Below shows an example of a matrix with a length of 3 being LU factorized using the routine
 "matrix_LU_factor". 

      matrix = [[1.0,1.0,-1.0],[1.0,-2.0,3.0],[2.0,3.0,1.0]]
      matrix_new = matrix_LU_factor(matrix)
      for i in range(0,len(matrix)):
          print(matrix_new[0][i])
      for i in range(0,len(matrix)):
          print(matrix_new[1][i])

Output from the lines above:

      [1.0, 0, 0]
      [1.0, 1.0, 0]
      [2.0, -0.3333333333333333, 1.0]
	  
      [1.0, 1.0, -1.0]
      [0.0, -3.0, 4.0]
      [0.0, 0.0, 4.333333333333333]

The two matrices printed above are the lower-triangle and upper-triangle matrices that satisfy LU = A (Where A is the original matrix).

**Implementation/Code:** The following is the code for matrix_LU_factor()


      import copy
      
      def matrix_LU_factor(matrix):
          n = len(matrix)
          u_matrix = copy.deepcopy(matrix)
          l_matrix = [[0 for i in range(n)] for j in range(n)]
          for k in range(0,n):
              for i in range(k+1, n):
                  l_matrix[i][k] = u_matrix[i][k] / u_matrix[k][k]
                  for j in range(k + 1, n):
                      u_matrix[i][j] -= l_matrix[i][k]*u_matrix[k][j]
          for i in range(n):
              l_matrix[i][i] = 1.0
          for i in range(1,n):
              for j in range(0, i):
                  u_matrix[i][j] = 0.0
      
          return [l_matrix,u_matrix]

