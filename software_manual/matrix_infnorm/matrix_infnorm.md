# Software Manual (matrix_infnorm.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_infnorm.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will calculate the infinity-norm of a matrix. The infinity-norm of a matrix is
 given by the formula: matrix_infnorm = largest components in the matrix.

**Input:** argument1: The matrix that we will calcualte the infinity-norm of.

**Output:** This routine returns the infinity-norm of the matrix given.

**Usage/Example:**

Below shows an example of finding the infinity-norm of a matrix with a length of 5 using the routine "matrix_infnorm". 

      matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
      print(matrix_infnorm(matrix))

Output from the lines above:

      125.0

The above number printed is the infinity-norm of the given matrix.

**Implementation/Code:** The following is the code for matrix_infnorm()


      def matrix_infnorm(matrix):
          temp_list = []
          for i in range(len(matrix)):
              sum = 0.0
              for j in range(len(matrix[0])):
                  sum += abs(matrix[i][j])
              temp_list.append(sum)
      
          return max(temp_list)
