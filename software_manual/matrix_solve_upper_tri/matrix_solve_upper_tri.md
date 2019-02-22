# Software Manual (matrix_solve_upper_tri.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_upper_tri.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations where the
 coefficient matrix is an upper triangle matrix. (The system is of the form Ax = b)

**Input:** argument1: The upper triangle matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_upper_tri".
 Then the solution vector is printed. 

      matrix = [[4,8,10,3,7],[0,2,5,7,2],[0,0,2,7,3],[0,0,0,3,1],[0,0,0,0,8]]
      vector = [12,25,38,27,48]
      print(matrix_solve_upper_tri(matrix,vector))

Output from the lines above:

      [-13.0, 18.25, -14.5, 7.0, 6.0]

In the example above, the upper triangle matrix representing "A" in the system "Ax = b" had a width of "5". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_upper_tri()
      
      def matrix_solve_upper_tri(matrix,vector):
      
          n = len(matrix)
          solution = [0]*len(vector)
      
          for i in range(n-1, -1, -1):
              temp_var = vector[i]
              for j in range(i+1, n):
                  temp_var -= matrix[i][j] * solution[j]
              solution[i] = temp_var/matrix[i][i]
      
          return solution
