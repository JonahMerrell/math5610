# Software Manual (matrix_find_eigenvalues.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_find_eigenvalues.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will attempt to find all of the eigenvalues of a given matrix by first 
computing the smallest and largest eigenvalues using the power iteration and inverse power iteration method, 
and then using shifting to find eigenvalues inbetween.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   
**Output:** This routine returns a list of the eigenvalues of the matrix.

**Usage/Example:**

Below shows an example of finding the eigenvalues of a matrix by using the routine "matrix_find_eigenvalues".
 Then the solution vector is printed. 

      matrix_example = [[7,1,1],[3,1,2],[1,3,2]]
      print(matrix_find_eigenvalues(matrix_example))

Output from the lines above:

      [-1.0000000000000049, 8.000000000030333, 3.000000000000001]

In the example above, the matrix representing "A" has a width of "3". The output represents the 3 eigenvalues of A.

**Implementation/Code:** The following is the code for matrix_find_eigenvalues()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_inverse_power_iteration, matrix_power_iteration
      
      def matrix_find_eigenvalues(matrix):
          eigenvalues = []
          eigenvalues.append(matrix_inverse_power_iteration(matrix,0.56,0.00000000000001,20000))
          eigenvalues.append(matrix_power_iteration(matrix,0.0000000001,20000))
          find_middle_eigenvalue(matrix,eigenvalues,eigenvalues[0],eigenvalues[1])
          return eigenvalues
      
      def find_middle_eigenvalue(matrix,eigenvalues,min_value,max_value):
          middle = (max_value + min_value) / 2
          middle_eigenvalue, count = matrix_inverse_power_iteration(matrix, middle, 0.00000000000001, 1000,getIterCount=True)
          if (count != 1000):#If no convergence happens after 1000 iterations, then middle is probably right inbetween the only 2 eigenvalues.
              if (not abs(middle_eigenvalue - min_value) < 0.0001) and (not abs(middle_eigenvalue - max_value) < 0.0001):
                  eigenvalues.append(middle_eigenvalue)
                  find_middle_eigenvalue(matrix, eigenvalues, min_value, middle_eigenvalue)
                  find_middle_eigenvalue(matrix, eigenvalues, middle_eigenvalue, max_value)
