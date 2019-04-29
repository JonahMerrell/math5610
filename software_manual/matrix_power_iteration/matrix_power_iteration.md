# Software Manual (matrix_power_iteration.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_power_iteration.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will approximate the largest eigenvalue of a matrix using the Power Iteration algorithm. 
 The intial guess (x_0) to start off our iteration is arbitrarily chosen to be the first row of the matrix.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
           argument2: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument3: The maximum iterations allowed while iterating.<br>
		   
**Output:** This routine returns the largest eigenvalue of the matrix given as the first parameter.

**Usage/Example:**

Below shows an example of finding the lagest eigenvalue of a matrix by using the routine "matrix_power_iteration".
 Then the solution vector is printed. 

      matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
      print(matrix_power_iteration(matrix_example,0.00000001,10000))

Output from the lines above:

      7.561552811795219

In the example above, the matrix representing "A" has a width of "3". The output represents the largest eigenvalue of A.

**Implementation/Code:** The following is the code for matrix_power_iteration()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose
      
      
      def matrix_power_iteration(matrix,tol,max_iter):
          error = tol * 10
          count = 0
          eigenvaluenew = 1
          v_i = convert_vec_mat(matrix[0])
          while error > tol and count < max_iter:
              eigenvalueold = eigenvaluenew
              v_i = matrix_mult(matrix, v_i)
              v_i = matrix_scal_mult(1/vector_2norm(convert_vec_mat(v_i)),v_i)
              eigenvaluenew = matrix_mult(matrix_transpose(v_i),matrix_mult(matrix,v_i))[0][0]
              count += 1
              error = abs(eigenvaluenew - eigenvalueold)
          return eigenvaluenew
