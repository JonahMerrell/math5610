# Software Manual (matrix_solve.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_least_square.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by using the least squares method to change the problem into the form A^tAx = A^tb. Then the system is solved using traditional row-elimination and back-substitution methods.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_least_square".
 Then the solution vector is printed. 

      matrix_example = [[2,-1],[1,2],[1,1]]
      vector_example = [2,1,4]
      print(matrix_solve_least_square(matrix_example,vector_example))

Output from the lines above:

      [1.4285714285714286, 0.4285714285714286]

In the example above, the matrix "A" in the system "Ax = b" has 3 linearly independant rows but only 2 columns, meaning that the system has no exact solution. Using the least-squares method, the closest solution possible is found.
 Thus, the solution "x" returned above is the solution for x that has the smallest residual.

**Implementation/Code:** The following is the code for matrix_solve()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_mult, matrix_solve , matrix_transpose
      
      
      def matrix_solve_least_square(matrix,vector):
          vector = [[vector[i]] for i in range(len(vector))]
          matrix_A_At = matrix_mult(matrix_transpose(matrix),matrix)
          vector_At_b = matrix_mult(matrix_transpose(matrix),vector)
          solution = matrix_solve(matrix_A_At,[vector_At_b[i][0] for i in range(len(vector_At_b))])
          return solution
 