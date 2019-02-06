# Software Manual (abs_error.py)

## [Back](../softwaremanual)

**Routine Name:**           abs_error.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the absolute error of an approximation of a number, given the
 true value and approximation. The formula for calcualting the absolute error is: abs_error = abs(true_value - appr_value)

**Input:** argument1: The true value
		   argument2: The approximation to the true value

**Output:** This routine returns a the absolute error of the approximation given.

**Usage/Example:**

Since the routine returns the absolute error of an approximation, then we must provide it with our approximation, as well
 as the true value (in order to make the comparison). Below shows an example:

      print(abs_error(1.0,1.00001)

Output from the line above:

      1.3199999999935486e-05

The above value (printed as the output) represents the absolute error of the approximation to the true value given in the input.

**Implementation/Code:** The following is the code for abs_error()


      def abs_error(true_value,appr_value):
          abs_error_value = abs(true_value - appr_value)
          return abs_error_value
