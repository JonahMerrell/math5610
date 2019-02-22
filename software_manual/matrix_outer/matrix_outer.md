# Software Manual (matrix_outer.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_outer.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will return the outer product of two vectors.

**Input:** argument1: The first vector in the outer product<br>
		   argument2: The second vector in the outer product<br>
		   
**Output:** This routine returns a matrix that is obtained from the outer product of two vectors. 

**Usage/Example:**

Below shows an example of calcualting the outer product of 2 different vectors with a length of 5 using the routine.
 "matrix_outer". 

      #vector1 = [1,2,3,4,5]
      #vector2 = [6,7,8,9,10]
      #print(matrix_outer(vector1,vector2))

Output from the lines above:

      [[6, 7, 8, 9, 10], [12, 14, 16, 18, 20], [18, 21, 24, 27, 30], [24, 28, 32, 36, 40], [30, 35, 40, 45, 50]]

The above vector printed is the outer product of the previous 2 vectors provided.


**Implementation/Code:** The following is the code for matrix_outer()


      def matrix_outer(vector1,vector2):
          matrix_outer_product = [[0 for j in range(len(vector2))] for i in range(len(vector1))]
          for i in range(len(vector1)):
              for j in range(len(vector2)):
                  matrix_outer_product[i][j] = vector1[i] * vector2[j]
      
          return matrix_outer_product
