# Software Manual (abs_error_infnorm.py)

## [Back](../softwaremanual)

**Routine Name:**           abs_error_infnorm.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the the absolute error in the approximation of one vector by another when the infinity-norm is used.

**Input:** argument1: A vector that is the true value. <br>
		   argument2: A vector that is an approximation to the true value.

**Output:** This routine returns the infinity-norm of the absolute error of the approximation given.

**Usage/Example:**

Since the routine returns the 2-norm of the absolute error of an approximation, then we must provide it with our approximation vector, as well
 as the true value vector (in order to make the comparison). Below shows an example:

      vector1 = [5,7,9,2,5]
      vector2 = [5.1,7.2,8.7,2,5.15]
      print(abs_error_infnorm(vector1,vector2))

Output from the line above:

      0.3000000000000007

The above value (printed as the output) represents the infinity-norm of the absolute error of the approximation to the true value given in the input.

**Implementation/Code:** The following is the code for abs_error_infnorm()


      import math
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_infnorm, vector_add, vector_scal_mult
      
      
      def abs_error_infnorm(true_vector,appr_vector):
          error_vector = vector_add(true_vector,vector_scal_mult(-1,appr_vector))
          for i in range(len(error_vector)):
              error_vector[i] = abs(error_vector[i])
          abs_error = vector_infnorm(error_vector)
          return abs_error
