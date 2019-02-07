# Software Manual (vector_add.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_add.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will add to vectors together. More precisly speaking, this
 routine will add the corresponding componenets of 2 vectors together to obtain a third vector, which
 we consider to be the "sum" of the 2 original vectors.

**Input:** argument1: The first vector to be added<br>
		   argument2: The second vector to be added<br>
		   The 2 vectors given must have equal length.
		   
**Output:** This routine returns a vector that is obtained from the result of adding the
 corresponding componenents of 2 vectors together. 

**Usage/Example:**

Below shows an example of 2 different vectors with a length of 5 being added together using the routine
 "vector_add". 

      vector1 = [5,7,9,2,5]
      vector2 = [8,2,3,6,9]
      print(vector_add(vector1,vector2))

Output from the lines above:

      [13, 9, 12, 8, 14]

The above vector printed is the "sum" of the previous 2 vectors provided. For example, consider the first
 element in the 2 vectors given as input, "5" and "3". Since 5 + 3 = 8, this explains why the first element
 in the new vector produced by "vector_add" is "8". This is how the other 4 elements in the new vector
 were produced.

**Implementation/Code:** The following is the code for vector_add()


      def vector_add(vector1,vector2):
          vector_sum = [0]* len(vector1)
          for i in range(len(vector_sum)):
              vector_sum[i] = vector1[i] + vector2[i]
      
          return vector_sum
