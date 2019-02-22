# Software Manual (vector_scal_mult.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_scal_mult.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will multipy a vector by a scalar . More precisly speaking, this
 routine will multiply all of the components of a vector by a scalar.

**Input:** argument1: The scalar to be multiplied with the vector<br>
		   argument2: The vector to be multiplied
		   
**Output:** This routine returns a vector that is obtained from the result of multiplying all of its
  componenents by the scalar given. 

**Usage/Example:**

Below shows an example of a vector with a length of 5 being multiplied by 5 using the routine
 "vector_scal_mult". 

      vector = [5,7,9,2,5]
      print(vector_scal_mult(5,vector))

Output from the lines above:

      [25, 35, 45, 10, 25]

The above vector printed is the 5 times greater then the original vector provided. For example, consider the second
 element in the vector given as input, "7" . Since 7 * 5 = 35, this explains why the second element
 in the new vector produced by "vector_scal_mult" is "35". This is how the other 4 elements in the new vector
 were produced.

**Implementation/Code:** The following is the code for vector_scal_mult()


      def vector_scal_mult(scalar,vector):
          vector_new = vector.copy()
          for i in range(len(vector)):
              vector_new[i] *= scalar
      
          return vector_new
