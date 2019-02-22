# Software Manual (vector_cross.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_cross.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will return the cross product of 2 vectors. The routine only 
works for vectors with a length of 3.

**Input:** argument1: The first vector in the cross product<br>
		   argument2: The second vector in the cross product<br>
		   The 2 vectors given must have length 3.
		   
**Output:** This routine returns a vector that is obtained from the cross product of two vectors. 

**Usage/Example:**

Below shows an example of calcualting the cross product of 2 different vectors with a length of 3 using the routine.
 "vector_cross". 

      vector1 = [5,7,9]
      vector2 = [8,2,3]
      print(vector_cross(vector1,vector2))

Output from the lines above:

      [3, 57, -46]

The above vector printed is the cross product of the previous 2 vectors provided. In this example, the exact 
calculation performed was [7*3 - 9*2, 8*9 - 5*3 ,5*2 - 8*7].


**Implementation/Code:** The following is the code for vector_cross()


      def vector_cross(vector1,vector2):
          vector_crossed = [0,0,0]
          vector_crossed[0] = vector1[1] * vector2[2] - vector1[2] * vector2[1]
          vector_crossed[1] = vector1[2] * vector2[0] - vector1[0] * vector2[2]
          vector_crossed[2] = vector1[0] * vector2[1] - vector1[1] * vector2[0]
      
          return vector_dotted
