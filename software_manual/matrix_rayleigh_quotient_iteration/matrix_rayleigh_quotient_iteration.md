# Software Manual (matrix_rayleigh_quotient_iteration.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_rayleigh_quotient_iteration.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will find an eigenvector of a matrix using the rayleigh quotient iteration.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
           argument2: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument3: The maximum iterations allowed while iterating.<br>
		   argument4: An optional parameter "getIterCount" set to false by default. (See output for details)
		   
**Output:** This routine returns an eigenvalue of a matrix (inputted in the first parameter). If "getIterCount" was set to true, then the routine
 will also output the number of iterations done to compute the eigenvalue.

**Usage/Example:**

Below shows an example of finding an eigenvalue of a matrix by using the routine "matrix_rayleigh_quotient_iteration".
 Then the eigenvalue is printed. 

      matrix_example = [[-16,9,0,0],[-12,5,0,0],[0,0,6,-2],[0,0,0,4]] #-7, -4, 4, 6
      print(matrix_rayleigh_quotient_iteration(matrix_example,0.0000000000001,20000))


Output from the lines above:

      -6.999999999999995

In the example above, the matrix representing "A" has a width of "4". The output represents one of the eigenvalues of A.

**Implementation/Code:** The following is the code for matrix_rayleigh_quotient_iteration()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_scal_mult, vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose, matrix_solve_LU, matrix_add
      
      
      def matrix_rayleigh_quotient_iteration(matrix,tol,max_iter,getIterCount=False):
          error = tol * 10
          count = 0
          v_i = matrix[0]
          v_i = vector_scal_mult(1 / vector_2norm(v_i), v_i)
          eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)), matrix_mult(matrix, convert_vec_mat(v_i)))[0][0]
          I = [[int(i == j) for i in range(len(matrix))] for j in range(len(matrix))]
      
          while error > tol and count < max_iter:
              eigenvalueold = eigenvaluenew
              v_i = matrix_solve_LU(matrix_add(matrix,matrix_scal_mult(-eigenvaluenew,I)),v_i)
              v_i = vector_scal_mult(1/vector_2norm(v_i),v_i)
              eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)), matrix_mult(matrix, convert_vec_mat(v_i)))[0][0]
              error = abs(eigenvaluenew - eigenvalueold)
              count += 1
          if getIterCount == True:
              return eigenvaluenew,count
          else:
              return eigenvaluenew
