# Software Manual (matrix_QR_factorization.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_QR_factorization.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine return the QR-factorization of a square matrix A. The 2 matrices Q and R returned from this routine satisfy QR = A (Where A is the original matrix, and Q satisfies Q^-1 = Q^t, and R is an upper triangle matrix).

**Input:** argument1: The matrix to perform QR factorization on<br>
		   
**Output:** This routine returns a list containing 2 elements. The first element is the
 "Q" matrix (satisfying Q^-1 = Q^t), and the second element is the "R" matrix (an upper triangle matrix).

**Usage/Example:**

Below shows an example of a matrix with a length of 3 being QR factorized using the routine
 "matrix_QR_factorization". 

      matrix_example = [[1,2,4],[0,0,5],[0,3,6]]
      matrix_new = matrix_QR_factorization(matrix_example)
      for i in range(0,len(matrix_new[0])):
          print(matrix_new[0][i])
      for i in range(0,len(matrix_new[1])):
          print(matrix_new[1][i])

Output from the lines above:

      [1.0, 0.0, 0.0]
      [0.0, 0.0, 1.0]
      [0.0, 1.0, 0.0]
	  
      [1.0, 2.0, 4.0]
      [0.0, 3.0, 6.0]
      [0.0, 0.0, 5.0]

The two matrices printed above are the Q and R matrices that satisfy QR = A (Where A is the original matrix).

**Implementation/Code:** The following is the code for matrix_QR_factorization()


      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_dot, vector_scal_mult, vector_add, vector_2norm, matrix_mult, matrix_transpose
      
      def matrix_QR_factorization(matrix):
          matrix_columns = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
          u_vectors = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
          for j in range(len(matrix[0])):
              for i in range(j):
                  u_vectors[j] = vector_add(u_vectors[j],vector_scal_mult(-1 * vector_dot(matrix_columns[j], u_vectors[i]), u_vectors[i]))
              u_vectors[j] = vector_scal_mult(1 / vector_2norm(u_vectors[j]), u_vectors[j])
      
          matrix_Q = [[u_vectors[i][j] for i in range(len(u_vectors))] for j in range(len(u_vectors[0]))]
          matrix_R = matrix_mult(matrix_transpose(matrix_Q), matrix)
      
          return [matrix_Q,matrix_R]


