# Software Manual (matrix_solve_conjugate_gradient.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_conjugate_gradient.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by the conjugate gradient iteration. The intial guess (x_0) to start off our iteration is arbitrarily chosen to be the b vector.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b<br>
           argument3: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument4: The maximum iterations allowed while iterating.<br>
		   
**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_conjugate_gradient".
 Then the solution vector is printed. 

      matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
      vector_example = [1, 2, 3]
      print(matrix_solve_conjugate_gradient(matrix_example,vector_example,0.00001,1000))

Output from the lines above:

      [-0.10256410256410224, 0.38461538461538497, 0.5641025641025642]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "3". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_conjugate_gradient()
      
      def matrix_solve_conjugate_gradient(matrix,vector_b,tol,max_iter):
          error = tol * 10
          count = 0
          x_i = vector_b.copy()  # x_0
          residual = vector_add(vector_b, vector_scal_mult(-1, convert_vec_mat(matrix_mult(matrix, convert_vec_mat(x_i)))))
          direction = residual
          d1new = vector_dot(residual, residual)
      
          while error > tol and count < max_iter:
              s = convert_vec_mat(matrix_mult(matrix,convert_vec_mat(direction)))
              d1old = d1new
              alpha = d1old / vector_dot(direction, s)
              x_i = vector_add(x_i,vector_scal_mult(alpha,direction))
              residual = vector_add(residual,vector_scal_mult(-alpha, s))
              d1new = vector_dot(residual, residual)
              direction = vector_add(residual,vector_scal_mult(d1new/d1old,direction))
              count += 1
              error = vector_2norm(residual)
          return x_i
