# Software Manual (matrix_solve_diagonal.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_diagonal.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations where the
 coefficient matrix is a diagonal matrix. (The system is of the form Ax = b)

**Input:** argument1: The diagonal matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_diagonal".
 Then the solution vector is printed. 

      matrix = [[4,0,0,0,0],[0,5,0,0,0],[0,0,2,0,0],[0,0,0,3,0],[0,0,0,0,8]]
      vector = [12,25,38,27,48]
      print(matrix_solve_diagonal(matrix,vector))

Output from the lines above:

      [3.0, 5.0, 19.0, 9.0, 6.0]

In the example above, the diagonal matrix representing "A" in the system "Ax = b" had a width of "5". The output vector "x" is the solution 
vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_diagonal()
      
      def matrix_solve_diagonal(matrix,vector):
          width = len(matrix)
          solution = [0]*len(vector)
      
          for i in range(width):
              solution[i] = vector[i]/matrix[i][i]
      
          return solution
