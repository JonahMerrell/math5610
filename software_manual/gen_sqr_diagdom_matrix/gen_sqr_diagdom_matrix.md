# Software Manual (gen_sqr_diagdom_matrix.py)

## [Back](../softwaremanual)

**Routine Name:**           gen_sqr_diagdom_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n diagonaly dominant square matrix (the size is
 inputted from the user). In order to make the matrix diagonaly dominant, random entries from 0 to 1 
 are generated everywhere in the matrix. Then, to make the matrix diagonally dominant, the diagonal entries
 in the matrix are set te be the sum of the other entries on the same row.

**Input:** There are no inputs needed in this case. However, the routine itself will prompt the following to the user 
"Please enter the width of the matrix: "  So in this sense, there is in fact an input needed, where the input 
(given by the user) will determine the size of the matrix generated.

**Output:** This routine returns the n*n diagnaly dominant square matrix generated of the size specified
 from the user.

**Usage/Example:**

Below shows an example of generating a matrix using the routine "gen_sqr_diagdom_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = gen_sqr_diagdom_matrix()
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      Please enter the width of the square matrix: 5
     [2.9196600530934473, 0.5886252052081804, 0.8123341006490915, 0.25344432985857646, 0.9349509386325648]
     [0.16861679650311745, 1.8296717025377205, 0.8126364850225107, 0.10220247296624574, 0.7068847784465977]
     [0.5077437798889743, 0.10813724894292132, 1.4678906809555903, 0.04466773911282451, 0.1766957111925549]
     [0.21727873917212948, 0.4850126127153802, 0.05006661081955288, 2.1516301528070136, 0.9782452209232437]
     [0.3027402153814376, 0.37937255594245967, 0.8385021195928042, 0.5554609423543404, 2.5074457248069217]

In the example above, "5" was chosen to be the width of the sqaure matrix.
 The above matrix generated is just one possible matrix generated, since the content of the matrix is generated randomly.
 Calling this function again would (likely) produce a matrix with different randomly generated numbers inside. You
  can observe that the entries on the diagnal of the matrix are larger (relativly speaking), because the matrix is
  diagnoly dominant.

**Implementation/Code:** The following is the code for gen_sqr_diagdom_matrix()


      import random
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_1norm
      
      def gen_sqr_diagdom_matrix():
          width = int(input("Please enter the width of the square matrix: "))
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(0, width):
                  value = random.random()
                  A[j][i] = value
      
          for i in range(0, width):
              value = vector_1norm(A[i])
              A[i][i] = value
          return A
