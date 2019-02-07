# Software Manual (matrix_mult.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_mult.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will calculate perform matrix multiplication on 2 matrices.

**Input:** argument1: The first matrix to be multiplied<br>
		   argument2: The second matrix to be multiplied<br>

**Output:** This routine returns a matrix resulting from multiplying the 2 matrices given together.

**Usage/Example:**

Below shows an example of performing matrix multiplication using the routine "matrix_mult". 

      vector1 = [[2,1,4],[0,1,1]]
      vector2 = [[6,3,-1,0],[1,1,0,4],[-2,5,0,2]]
      print(matrix_mult(vector1,vector2))

Output from the lines above:

      [[5, 27, -2, 12], [-1, 6, 0, 6]]

The above matrix printed is the result of the given matrix multiplication.

**Implementation/Code:** The following is the code for matrix_mult()


      def matrix_mult(vector1,vector2):
          iter_count = len(vector1[0]) # = len(vector2)
          width = len(vector2[0])
          height = len(vector1)
          final_matrix = [[0 for i in range(width)] for j in range(height)]
      
          for i in range(width):
              for j in range(height):
                  sum = 0
                  for k in range(iter_count):
                      sum += vector1[j][k]*vector2[k][i]
                  final_matrix[j][i] = sum
      
          return final_matrix
