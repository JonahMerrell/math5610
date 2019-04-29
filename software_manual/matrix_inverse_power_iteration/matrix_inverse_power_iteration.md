# Software Manual (matrix_inverse_power_iteration.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_inverse_power_iteration.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will approximate the smallest eigenvalue of a matrix using the inverse power iteration algorithm. 
The intial guess (x_0) to start off our iteration is arbitrarily chosen to be the first row of the matrix.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
           argument2: The amount of shifting to apply to the inverse power iteration to find other eigenvalues.<br>
		   argument3: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument4: The maximum iterations allowed while iterating.<br>
		   argument5: An optional parameter "getIterCount" set to false by default. (See output for details)
		   
**Output:** This routine returns the smallest eigenvalue of the shifted matrix. If "getIterCount" was
 set to true, then the routine will also output the number of iterations done to compute x.

**Usage/Example:**

Below shows an example of finding the smallest eigenvalue of a shifted matrix by using the routine "matrix_inverse_power_iteration".
 Then the eigenvalue is printed.

      matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
      print(matrix_inverse_power_iteration(matrix_example,0,0.0000000000001,20000))

Output from the lines above:

      3.0000000000002522

In the example above, the matrix representing "A" has a width of "3". The output represents the smallest eigenvalue of A. (Since the 
shift was 0).

**Implementation/Code:** The following is the code for matrix_inverse_power_iteration()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_scal_mult, matrix_mult, convert_vec_mat, vector_2norm, matrix_transpose, matrix_solve_LU, matrix_add
      
      
      def matrix_inverse_power_iteration(matrix,alpha,tol,max_iter,getIterCount=False):
          error = tol * 10
          count = 0
          eigenvaluenew = 0
          I = [[-int(i == j)*alpha for i in range(len(matrix))] for j in range(len(matrix))]
          v_i = matrix[0]
          while error > tol and count < max_iter:
      
              eigenvalueold = eigenvaluenew
              v_i = matrix_solve_LU(matrix_add(matrix,I),v_i)
              v_i = vector_scal_mult(1/vector_2norm(v_i),v_i)
              eigenvaluenew = matrix_mult(matrix_transpose(convert_vec_mat(v_i)),matrix_mult(matrix,convert_vec_mat(v_i)))[0][0]
              count += 1
              error = abs(eigenvaluenew - eigenvalueold)
          if getIterCount == True:
              return eigenvaluenew,count
          else:
              return eigenvaluenew

