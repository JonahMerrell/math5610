# Software Manual (matrix_add.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_add.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will add to matrices together. More precisly speaking, this
 routine will add the corresponding componenets of 2 matrices together to obtain a third matrix, which
 we consider to be the "sum" of the 2 original matrices.

**Input:** argument1: The first matrix to be added<br>
		   argument2: The second matrix to be added<br>
		   The 2 matrices given must have equal dimensions.
		   
**Output:** This routine returns a matrix that is obtained from the result of adding the
 corresponding componenents of 2 matrices together. 

**Usage/Example:**

Below shows an example of 2 different matrices with a length of 5 being added together using the routine
 "matrix_add". 

      matrix1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
      matrix2 = [[26,27,28,29,30],[31,32,33,34,35],[36,37,38,39,40],[41,42,43,44,45],[46,47,48,49,50]]
      print(matrix_add(matrix1,matrix2))

Output from the lines above:

      [[27, 29, 31, 33, 35], [37, 39, 41, 43, 45], [47, 49, 51, 53, 55], [57, 59, 61, 63, 65], [67, 69, 71, 73, 75]]

The above matrix printed is the "sum" of the previous 2 matrices provided.

**Implementation/Code:** The following is the code for matrix_add()


      def matrix_add(matrix1,matrix2):
          matrix_sum = [[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]
          for i in range(len(matrix_sum)):
              for j in range(len(matrix_sum[0])):
                  matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j]
      
          return matrix_sum
