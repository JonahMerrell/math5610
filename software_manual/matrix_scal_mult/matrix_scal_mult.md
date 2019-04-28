# Software Manual (matrix_scal_mult.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_scal_mult.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will multipy a matrix by a scalar . More precisly speaking, this
 routine will multiply all of the components of a matrix by a scalar.

**Input:** argument1: The scalar to be multiplied with the matrix<br>
		   argument2: The matrix to be multiplied
		   
**Output:** This routine returns a matrix that is obtained from the result of multiplying all of its
  componenents by the scalar given. 

**Usage/Example:**

Below shows an example of a matrix with a length of 5 being multiplied by 5 using the routine
 "matrix_scal_mult". 

      matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
      print(matrix_scal_mult(5,matrix))

Output from the lines above:

      [[5, 10, 15, 20, 25], [30, 35, 40, 45, 50], [55, 60, 65, 70, 75], [80, 85, 90, 95, 100], [105, 110, 115, 120, 125]]

The above matrix printed is the 5 times greater then the original matrix provided. For example, consider the second
 row in the matrix given as input, "[6,7,8,9,10]" . After multiplying by 5 in this example, the second element
 in the new matrix produced by "matrix_scal_mult" is "[30, 35, 40, 45, 50]". This is true for all the components of the matrix.

**Implementation/Code:** The following is the code for matrix_scal_mult()


      def matrix_scal_mult(scalar,matrix):
          matrix_new = [[scalar*matrix[j][i] for i in range(len(matrix[0]))] for j in range(len(matrix))]
      
          return matrix_new


