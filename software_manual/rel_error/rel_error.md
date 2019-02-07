# Software Manual (rel_error.py)

## [Back](../softwaremanual)

**Routine Name:**           rel_error.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the relative error of an approximation of a number, given the
 true value and approximation. The formula for calcualting the relative error is: rel_error = rel_error = abs((true_value - appr_value)/true_value)

**Input:** argument1: The true value<br>
		   argument2: The approximation to the true value

**Output:** This routine returns a the relative error of the approximation given (as a float).

**Usage/Example:**

Since the routine returns the relative error of an approximation, then we must provide it with our approximation, as well
 as the true value (in order to make the comparison). Below shows an example:

      print(rel_error(1.0,1.0000132)

Output from the line above:

      1.3199999999935486e-05

The above value (printed as the output) represents the relative error of the approximation to the true value given in the input.

**Implementation/Code:** The following is the code for rel_error()


      def rel_error(true_value,appr_value):
          rel_error_value = abs((true_value - appr_value)/true_value)
          return rel_error_value
