# Software Manual (gen_diagdom_sym_matrix.py)

## [Back](../softwaremanual)

**Routine Name:**           gen_diagdom_sym_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n diagnaly dominant symmetric square matrix (the size is
 inputted from the user). In order to make the matrix diagnaly dominant, random entries from 0 to 1 
 are generated everywhere in the matrix. Then, to make the matrix diagnally dominant, the diagnal entries
 in the matrix are set te be the sum of the other entries on the same row.

**Input:** There are no inputs needed in this case. However, the routine itself will prompt the following to the user 
"Please enter the width of the matrix: "  So in this sense, there is in fact an input needed, where the input 
(given by the user) will determine the size of the matrix generated.

**Output:** This routine returns the n*n diagnaly dominant symmetric square matrix generated of the size specified
 from the user.

**Usage/Example:**

Below shows an example of generating a matrix using the routine "gen_diagdom_sym_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = gen_diagdom_sym_matrix()
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      Please enter the width of the square matrix: 5
      [2.1686859940646395, 0.8473293050013687, 0.702280847044595, 0.25588775434827393, 0.051176151322430585]
      [0.8473293050013687, 2.717600619502754, 0.998373163569946, 0.47126097668799805, 0.26977952768708713]
      [0.702280847044595, 0.998373163569946, 3.0753258185638095, 0.4120788519849855, 0.034849661649295705]
      [0.25588775434827393, 0.47126097668799805, 0.4120788519849855, 2.069053466727718, 0.44984363483811696]
      [0.051176151322430585, 0.26977952768708713, 0.034849661649295705, 0.44984363483811696, 1.0487422657583516]

In the example above, "5" was chosen to be the width of the sqaure matrix.
 The above matrix generated is just one possible matrix generated, since the content of the matrix is generated randomly.
 Calling this function again would (likely) produce a matrix with different randomly generated numbers inside. You
  can observe that the entries on the diagonal of the matrix are larger (relativly speaking), because the matrix is
  diagonoly dominant.

**Implementation/Code:** The following is the code for gen_diagdom_sym_matrix()


      import random

      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_1norm
      
      def gen_diagdom_matrix():
          width = int(input("Please enter the width of the square matrix: "))
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(i, width):
                  value = random.random()
                  A[j][i] = value
                  A[i][j] = value
          for i in range(0, width):
              value = vector_1norm(A[i])
              A[i][i] = value
          return A
