# Software Manual (matrix_QR_factorization_mod.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_QR_factorization_mod.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine return the QR-factorization (using the modified Gram-Schmidt algorithm) of a square matrix A. The 2 matrices Q and R returned from this routine satisfy QR = A (Where A is the original matrix, and Q satisfies Q^-1 = Q^t, and R is an upper triangle matrix).

**Input:** argument1: The matrix to perform QR factorization on<br>
		   
**Output:** This routine returns a list containing 2 elements. The first element is the
 "Q" matrix (satisfying Q^-1 = Q^t), and the second element is the "R" matrix (an upper triangle matrix).

**Usage/Example:**

Below shows an example of a matrix with a length of 3 being QR factorized using the routine
 "matrix_QR_factorization_mod". 

      matrix_example = [[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]]
      matrix_new = matrix_QR_factorization_mod(matrix_example)
      for i in range(0,len(matrix_new[0])):
          print(matrix_new[0][i])
      for i in range(0,len(matrix_new[1])):
          print(matrix_new[1][i])
      print(matrix_mult(matrix_new[0],matrix_new[1]))

Output from the lines above:

      [1.0, 0.0, 0.0]
      [0.0, 0.0, 1.0]
      [0.0, 1.0, 0.0]
	  
      [1.0, 2.0, 4.0]
      [0.0, 3.0, 6.0]
      [0.0, 0.0, 5.0]

The two matrices printed above are the Q and R matrices that satisfy QR = A (Where A is the original matrix).

**Implementation/Code:** The following is the code for matrix_QR_factorization_mod()


      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_dot, vector_scal_mult, vector_add, vector_2norm, matrix_mult, matrix_transpose
      
      def matrix_QR_factorization_mod(matrix):
      
          u_vectors = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
          print(u_vectors)
          for j in range(len(matrix[0])):
              for i in range(j):
                  u_vectors[j] = vector_add(u_vectors[j],vector_scal_mult(-1 * vector_dot(u_vectors[j], u_vectors[i]), u_vectors[i]))
              u_vectors[j] = vector_scal_mult(1 / vector_2norm(u_vectors[j]), u_vectors[j])
      
          matrix_Q = [[u_vectors[i][j] for i in range(len(u_vectors))] for j in range(len(u_vectors[0]))]
          matrix_R = matrix_mult(matrix_transpose(matrix_Q), matrix)
      
          return [matrix_Q,matrix_R]

