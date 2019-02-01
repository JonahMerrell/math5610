# Software Manual (gen_rand_matrix.py)

## [Back](../softwaremanual)

**Routine Name:**           gen_rand_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*m matrix (the size is inputted from the user)
 with random entries from 0 to 1.

**Input:** There are no inputs needed in this case. However, the routine itself will prompt the following to the user 
"Please enter the width of the matrix: " and "Please enter the height of the matrix: " . So in this sense, there is in
 fact an input needed, where the input (given by the user) will determine the size of the matrix generated.

**Output:** This routine returns the n*m matrix generated of the size specified from the user.

**Usage/Example:**

Below shows an example of generating a matrix using the routine "gen_rand_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = generate_sym_matrix()
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      Please enter the width of the matrix: 4
      Please enter the height of the matrix: 6
      [0.18361695228266373, 0.24419516412171816, 0.6462210640959352, 0.37810880655946166]
      [0.06450890123439323, 0.8157962192772203, 0.4892644472021095, 0.7642990862352379]
      [0.9004559438860636, 0.21503714922621286, 0.26971632524829736, 0.6306694825635641]
      [0.6187029394329355, 0.8773015910518385, 0.31064448692689783, 0.22036563737472858]
      [0.36040852311262106, 0.7086674426489017, 0.23155806392035239, 0.2122329840992918]
      [0.0296720391881804, 0.4168391258833416, 0.6405902767713764, 0.9064789321201884]

In the example above, "4" was chosen to be the width of the matrix, and "6" was chosen to be the width of the matrix.
 The above matrix generated is just one possible matrix generated, since the content of the matrix is generated randomly.
 Calling this function again would (likely) produce a matrix with different randomly generated numbers inside.

**Implementation/Code:** The following is the code for smaceps()


      import random
      
      def generate_random_matrix():
          width = int(input("Please enter the width of the matrix: "))
          height = int(input("Please enter the height of the matrix: "))
          A = [[0 for i in range(width)] for j in range(height)]
          for i in range(0,width):
              for j in range(0, height):
                  A[j][i] = random.random()
          return A
