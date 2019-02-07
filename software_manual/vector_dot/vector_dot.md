# Software Manual (vector_dot.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_dot.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will return the dot product of 2 vectors. 

**Input:** argument1: The first vector in the dot product<br>
		   argument2: The second vector in the dot product<br>
		   The 2 vectors given must have equal length.
		   
**Output:** This routine returns a number that is obtained from the dot produce of two vectors of the same length. 

**Usage/Example:**

Below shows an example of calcualting the dot product of 2 different vectors with a length of 5 using the routine.
 "vector_dot". 

      vector1 = [5,7,9,2,5]
      vector2 = [8,2,3,6,9]
      print(vector_dot(vector1,vector2))

Output from the lines above:

      138

The above vector printed is the dot product of the previous 2 vectors provided. In this example, the exact 
calculation performed was 5*8 + 7*2 + 9*3 + 2*6 + 5*9 = 138.


**Implementation/Code:** The following is the code for vector_dot()


      def vector_dot(vector1,vector2):
          vector_sum = 0
          for i in range(len(vector1)):
              vector_sum += vector1[i] * vector2[i]
      
          return vector_sum
