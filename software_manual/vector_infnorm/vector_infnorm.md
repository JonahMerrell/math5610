# Software Manual (vector_infnorm.py)

## [Back](../softwaremanual)

**Routine Name:**           vector_infnorm.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will calculate the infinity-norm of a vector. The infinity-norm of a vector is
 given by the formula: vector_infnorm = the component in the vector with the largest magnitude.

**Input:** argument1: The vector that we will calcualte the inifity-norm of.

**Output:** This routine returns the infinity-norm of the vector given (as a float).

**Usage/Example:**

Below shows an example of finding the infinity-norm of a vector with a length of 5 using the routine "vector_infnorm". 

      vector = [5,7,9,2,5]
      print(vector_infnorm(vector))


Output from the lines above:

      9.0

The above number printed is the 1-norm of the given vector.

**Implementation/Code:** The following is the code for vector_infnorm()


      def vector_infnorm(vector):
          temp_max = 0
          for i in range(len(vector)):
              if temp_max < abs(vector[i]):
                  temp_max = abs(vector[i])
          return temp_max
