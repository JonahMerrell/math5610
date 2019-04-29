# Software Manual (matrix_condition_number_rayleigh_quotient.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_condition_number_rayleigh_quotient.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute an approximation of the condition number in the 2-norm using the 
rayleigh quotient routine in order to compute the largets eigenvector.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b
		   
**Output:** This routine returns an approximation of the condition number of a matrix.

**Usage/Example:**

Below shows an example of finding the condition number of a matrix using the routine "matrix_condition_number_rayleigh_quotient".
 Then the condition number is printed. 

      matrix_example = [[5, 1, 2], [1, 4, 1], [2, 1, 5]]
      print(matrix_condition_number_rayleigh_quotient(matrix_example,10000))
      
Output from the lines above:

      2.520517604266915

In the example above, the matrix representing "A" has a width of "3". The output represents an approximation for the condition number of A.

**Implementation/Code:** The following is the code for matrix_condition_number_rayleigh_quotient()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_condition_number_rayleigh_quotient, matrix_power_iteration
      
      def matrix_condition_number_rayleigh_quotient(matrix):
          smallest_eigenvalue = matrix_condition_number_rayleigh_quotient(matrix,0,0.000000000001,20000)
          largest_eigenvalue = matrix_power_iteration(matrix,0.00000000001,20000)
          return abs(largest_eigenvalue/smallest_eigenvalue)

