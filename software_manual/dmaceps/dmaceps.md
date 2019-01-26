# Software Manual (dmaceps.py)

## [Back](../softwaremanual)

**Routine Name:**           dmaceps.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of binary 
digits in the representation of real numbers in double precision. This is a routine for analyzing the behavior of any computer.
This usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. 

**Output:** This routine returns a list containing two elements: The first element in the list is the machine double float
mantissa, and the second element in the list is the machine double float precision.

**Usage/Example:**

Since the routine returns 2 values (machine mantissa and machine precision of a double precision arithmetic) in the form of a list,
then we must store the values recived into a list in order to use the 2 values seperatly. Below shows an example:

      dmaceps_data = calculate_double_float_precision()
      print("machine double float mantissa = " + str(dmaceps_data[0]))
      print("machine double float precision = " + str(dmaceps_data[1]))

Output from the lines above:

      machine double float mantissa = 53
      machine double float precision = 1.1102230246251565e-16

The first value (53) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the
end of the second value).

**Implementation/Code:** The following is the code for dmaceps()


      def calculate_double_float_precision():
          y = 1.0
          x = 1.0
          z = x + y
      
          error = abs(z - x)
          iteration_count = 0
      
          while (error > 0):
              y = y/2
              z = x + y
              error = abs(z - x)
              iteration_count += 1
      
          return [iteration_count,y]
