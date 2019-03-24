# Software Manual (gen_sym_posdef_matrix.py)

## [Back](../softwaremanual)

**Routine Name:**           gen_sym_posdef_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n symmetric positive-definite matrix (the size is inputted from the user)
 with random entries from 0 to 1.

**Input:** There are no inputs needed in this case. However, the routine itself will prompt the following to the user 
"Please enter the width of the square matrix: ". So in this sense, there is in fact an input needed, where the input 
(given by the user) will determine the size of the square symetric matrix generated.

**Output:** This routine returns the symetric n*n matrix generated of the size specified from the user.

**Usage/Example:**

Below shows an example of generating a symetric positive-definite matrix using the routine "gen_sym_posdef_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = gen_sym_posdef_matrix()
      for i in range(len(A_)):
          print(A_[i])

Output from the lines above:

      Please enter the width of the square matrix: 5
      [2.1299916128935443, 1.6552058122613746, 1.0669733563946053, 2.303370684810509, 2.1555965022580246]
      [1.6552058122613746, 1.7714872334525005, 1.0557926024679505, 1.9943425085828212, 1.7498183443173871]
      [1.0669733563946053, 1.0557926024679505, 1.221063943602681, 1.7310340736520864, 1.4262247484195203]
      [2.303370684810509, 1.9943425085828212, 1.7310340736520864, 3.2903144257120633, 2.5746650478275868]
      [2.1555965022580246, 1.7498183443173871, 1.4262247484195203, 2.5746650478275868, 2.3716161253944574]

In the example above, "5" was chosen to be the size of the matrix to be generated. The above matrix generated is just
 one possible matrix generated, since the content of the matrix is generated randomly.  Calling this function
 again would (likely) produce a matrix with different randomly generated numbers inside.

**Implementation/Code:** The following is the code for gen_sym_posdef_matrix()


      import random
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_mult
      
      def gen_sym_posdef_matrix():
          width = int(input("Please enter the width of the symmetric, positive definite matrix: "))
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(0, width):
                  value = random.random()
                  A[j][i] = value
          B = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(0, width):
                  B[j][i] = A[i][j]
      
          return matrix_mult(A,B)
