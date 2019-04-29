# Software Manual (matrix_solve_least_squares_QR_householder.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_least_squares_QR_householder.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by QR factorization using the householder transformations.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_least_squares_QR_householder".
 Then the solution vector is printed. 

      matrix_example = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
      vector_example = [12,25,38,27,48]
      print(matrix_solve_least_squares_QR_householder(matrix_example,vector_example))

Output from the lines above:

      [2.6226777706598434, -1.3299167200512514, -1.725816784112757, -1.1672005124920306, 6.659192825112138]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "5". The output vector "x"
 is the solution vector to the system, so that Ax = b. Using the least-squares QR factorization method, the closest solution possible is found.
 Thus, the solution "x" returned above is the solution for x that has the smallest residual.

**Implementation/Code:** The following is the code for matrix_solve_least_squares_QR_householder()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_QR_factorization_householder, matrix_solve_upper_tri, matrix_mult, matrix_transpose, convert_vec_mat
      
      
      def matrix_solve_least_squares_QR_householder(matrix,vector):
          (matrix_Q, matrix_R) = matrix_QR_factorization_householder(matrix)
          matrix_Qtb = matrix_mult(matrix_transpose(matrix_Q), convert_vec_mat(vector))
          solution = matrix_solve_upper_tri(matrix_R, convert_vec_mat(matrix_Qtb))
          return solution
 