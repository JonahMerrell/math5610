# Software Manual (vector_1norm.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_1norm.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will calculate the 1-norm of a vector. The 1-norm of a vector is
 given by the formula: vector_1norm = sum(x_1 + x_2 + x_3 + ... + x_n). (Where x_1,x_2,...
 x_n represent the components of the vector).

**Input:** argument1: The vector that we will calcualte the 1-norm of (as a float).

**Output:** This routine returns the 1-norm of the vector given.

**Usage/Example:**

Below shows an example of finding the 1-norm of a vector with a length of 5 using the routine "vector_1norm". 

      vector = [5,7,9,2,5]
      print(vector_1norm(vector))

Output from the lines above:

      28.0

The above number printed is the 1-norm of the given vector.

**Implementation/Code:** The following is the code for vector_1norm()


      def vector_1norm(vector):
          sum = 0.0
          for i in range(len(vector)):
              sum += abs(vector[i])
      
          return sum
