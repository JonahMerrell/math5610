# Software Manual (matrix_1norm.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_1norm.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will calculate the 1-norm of a matrix. The 1-norm of a matrix is
 given by the formula: matrix_1norm = sum(all the components in the matrix).

**Input:** argument1: The matrix that we will calcualte the 1-norm of.

**Output:** This routine returns the 1-norm of the matrix given.

**Usage/Example:**

Below shows an example of finding the 1-norm of a matrix with a length of 5 using the routine "matrix_1norm". 

      matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
      print(matrix_1norm(matrix))

Output from the lines above:

      75.0

The above number printed is the 1-norm of the given matrix.

**Implementation/Code:** The following is the code for matrix_1norm()


      def matrix_1norm(matrix):
          temp_list = []
          for j in range(len(matrix[0])):
              sum = 0.0
              for i in range(len(matrix)):
                  sum += abs(matrix[i][j])
              temp_list.append(sum)
      
          return max(temp_list)
