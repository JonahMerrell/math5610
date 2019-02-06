# Software Manual (vector_2norm.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_2norm.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will calculate the 2-norm of a vector. The 2-norm of a vector is
 given by the formula: vector_2norm = sum(x_1^2 + x_2^2 + x_3^2 + ... + x_n^2)^(1/2). (Where x_1,x_2,...
 x_n represent the components of the vector).

**Input:** argument1: The vector that we will calcualte the 2-norm of (as a float).

**Output:** This routine returns the 2-norm of the vector given.

**Usage/Example:**

Below shows an example of finding the 2-norm of a vector with a length of 5 using the routine "vector_2norm". 

      vector = [5,7,9,2,5]
      print(vector_2norm(vector))

Output from the lines above:

      13.564659966250536

The above number printed is the 2-norm of the given vector.

**Implementation/Code:** The following is the code for vector_2norm()

      import math
      
      def vector_2norm(vector):
          sum = 0.0
          for i in range(len(vector)):
              sum += (vector[i])*(vector[i])
          norm_2 = math.pow(sum,0.5)
      
          return norm_2
