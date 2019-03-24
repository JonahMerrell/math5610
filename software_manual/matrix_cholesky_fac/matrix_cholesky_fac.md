# Software Manual (matrix_cholesky_fac.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_cholesky_fac.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will perform the Cholesky factorization method for square matrices

**Input:** argument1: The matrix to perform cholesky factorization on.<br>

**Output:** This routine returns a matrix resulting from performing cholesky factorization on the input matrix given.

**Usage/Example:**

Below shows an example of performing cholesky factorization on a positive definate symetrical matrix using "matrix_cholesky_fac" (one row is printed at a time, for
 readabilities sake).

      A_ = matrix_cholesky_fac(gen_sym_posdef_matrix())
      A_ = matrix_cholesky_fac([[6,15,35],[15,55,225],[55,225,979]])
      for i in range(len(A_)):
          print(A_[i])

Output from the lines above:

      [2.449489742783178, 0, 0]
      [6.123724356957946, 4.183300132670377, 0]
      [22.45365597551247, 20.916500663351886, 6.110100926607785]

The above matrix printed is the cholesky-factorized result of the original matrix.

**Implementation/Code:** The following is the code for matrix_cholesky_fac()

      import copy
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_add, vector_scal_mult

      def matrix_cholesky_fac(matrix):
          n = len(matrix)
          #m = len(matrix[0])
          solution = copy.deepcopy(matrix)
          for i in range(0,n):
              for j in range(i+1, n):
                  if solution[i][i] !=0:
                      solution[j] = vector_add(solution[j],vector_scal_mult(-solution[j][i]/solution[i][i],solution[i]))
              solution[i] = vector_scal_mult(1/solution[i][i],solution[i])
          return solution
