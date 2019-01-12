# Math 4610 Fundamentals of Computational Mathematics Software Manual


**Routine Name:**           smaceps.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. 

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

      Simply just run smaceps.py

Output from the lines above:

machine single float mantissa = 23
machine single float precision = 5.9604645e-08

The first value (23) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-08 on the
end of the second value).


**Routine Name:**           dmaceps.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in double precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case. 

**Output:** This routine returns a double precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

      Simply just run dmaceps.py

Output from the lines above:

machine double float mantissa = 52
machine double float precision = 1.1102230246251565e-16

The first value (52) is the number of binary digits that define the machine epsilon and the second is related to the
decimal version of the same value. The number of decimal digits that can be represented is roughly eight (E-16 on the
end of the second value).

