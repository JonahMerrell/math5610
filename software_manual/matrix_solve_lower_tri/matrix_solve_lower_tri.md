# Software Manual (matrix_solve_lower_tri.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_lower_tri.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations where the
 coefficient matrix is an lower triangle matrix. (The system is of the form Ax = b)

**Input:** argument1: The lower triangle matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_lower_tri".
 Then the solution vector is printed. 

      matrix = [[8,0,0,0,0],[1,3,0,0,0],[3,7,2,0,0],[2,7,5,2,0],[7,3,10,8,4]]
      vector = [12,25,38,27,48]
      print(matrix_solve_lower_tri(matrix,vector))

Output from the lines above:

      [1.5, 7.833333333333333, -10.666666666666664, 11.249999999999993, 7.666666666666675]

In the example above, the lower triangle matrix representing "A" in the system "Ax = b" had a width of "5". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_lower_tri()
      
      def matrix_solve_lower_tri(matrix,vector):
          n = len(matrix)
          solution = [0]*len(vector)
      
          for i in range(0, n, 1):
              temp_var = vector[i]
              for j in range(i, -1, -1):
                  temp_var -= matrix[i][j] * solution[j]
              solution[i] = temp_var/matrix[i][i]
      
          return solution
