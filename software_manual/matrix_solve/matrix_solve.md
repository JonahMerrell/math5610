# Software Manual (matrix_solve.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by Gaussian elimination (elementary row operations) to reduce the augmented coefficient matrix "A" to row echelon form and then apply backsubstitution to find the solution. The gaussian elimination and backsubstitution processes are performed by 2 other methods, which are imported and implemented here to solve the system.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b

**Output:** This routine returns the solution vector "x" to the system of linear equations.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve".
 Then the solution vector is printed. 

      matrix_example = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
      vector_example = [12,25,38,27,48]
      print(matrix_solve(matrix_example,vector_example))

Output from the lines above:

      [2.6226777706598146, -1.3299167200512425, -1.7258167841127303, -1.1672005124919766, 6.659192825112087]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "5". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_ref, matrix_solve_upper_tri
      
      
      def matrix_solve(matrix,vector):
          n = len(matrix)
          solution = [0] * len(vector)
          for i in range(n):
              matrix[i].append(vector[i])
          ref_matrix = matrix_ref(matrix)
          for i in range(n):
              solution[i] = ref_matrix[i][-1]
              del ref_matrix[i][-1]
      
          solution = matrix_solve_upper_tri(ref_matrix,solution)
      
          return solution
