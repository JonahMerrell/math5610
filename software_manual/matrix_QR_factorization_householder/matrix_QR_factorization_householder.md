# Software Manual (matrix_QR_factorization_householder.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_QR_factorization_householder.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine return the QR-factorization (using householder transformations) of a square matrix A. The 2 matrices Q and R returned from this routine satisfy QR = A (Where A is the original matrix, and Q satisfies Q^-1 = Q^t, and R is an upper triangle matrix).

**Input:** argument1: The matrix to perform QR factorization on<br>
		   
**Output:** This routine returns a list containing 2 elements. The first element is the
 "Q" matrix (satisfying Q^-1 = Q^t), and the second element is the "R" matrix (an upper triangle matrix).

**Usage/Example:**

Below shows an example of a matrix with a length of 3 being QR factorized using the routine
 "matrix_QR_factorization_householder". 

      matrix_example = [[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]]
      matrix_new = matrix_QR_factorization_householder(matrix_example)
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

**Implementation/Code:** The following is the code for matrix_QR_factorization_householder()


      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_outer, matrix_add, matrix_scal_mult, vector_dot, vector_scal_mult, vector_add, vector_2norm, matrix_mult
      
      def matrix_QR_factorization_householder(matrix):
          matrix_R = [[matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))] #HA starts by being A
          matrix_Q = [[0 for j in range(len(matrix))] for k in range(len(matrix))] #Q starts by being the identity matrix
      
          for j in range(len(matrix)):
              matrix_Q[j][j] = 1
          for i in range(len(matrix[0])-1):
              a = [matrix_R[j][i] for j in range(len(matrix_R))] #a is the i'th column of matrix_R, with 0s inserted above the diagonal
              for j in range(i):
                  a[j] = 0
              r = [0]* len(a) #r is just a 0 vector, with the i'th column being the magnitude of a
              r[i] = vector_2norm(a)
              u = vector_add(a,vector_scal_mult(-1,r))
              i_ = [[0 for j in range(len(matrix))] for k in range(len(matrix))]
              for j in range(len(matrix)):
                  i_[j][j] = 1
              if vector_dot(u,u) != 0:
                  h = matrix_add(i_,matrix_scal_mult(-2/vector_dot(u,u),matrix_outer(u, u))) #computer h_i
              else: #if u ends up being the 0 matrix, then h is just the identity matrix
                  h = i_
              matrix_Q = matrix_mult(matrix_Q,h)
              matrix_R = matrix_mult(h,matrix_R)
      
          return [matrix_Q, matrix_R]

