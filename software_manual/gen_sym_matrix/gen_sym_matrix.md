# Software Manual (gen_sym_matrix.py)

## [Back](../softwaremanual)

**Routine Name:**           gen_sym_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n symmetric  matrix (the size is inputted from the user)
 with random entries from 0 to 1.

**Input:** There are no inputs needed in this case. However, the routine itself will prompt the following to the user 
"Please enter the width of the square matrix: ". So in this sense, there is in fact an input needed, where the input 
(given by the user) will determine the size of the square symetric matrix generated.

**Output:** This routine returns the symetric n*m matrix generated of the size specified from the user.

**Usage/Example:**

Below shows an example of generating a symet5ric matrix using the routine "gen_sym_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = generate_sym_matrix()
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      Please enter the width of the square matrix: 8
      [0.47160779814995213, 0.14968279049295208, 0.4248668394916504, 0.7520737851209678, 0.19134970045873145, 0.4813343166055776, 0.5063442768371293, 0.7976939280439258]
      [0.14968279049295208, 0.27111610286951704, 0.9475690120968813, 0.023319649066299908, 0.47739681800224787, 0.7642636799092533, 0.8545120485746511, 0.64167383494335]
      [0.4248668394916504, 0.9475690120968813, 0.8426383162987133, 0.00862922515959752, 0.7639644412685411, 0.23733729927123637, 0.6474221181599213, 0.3279445548632708]
      [0.7520737851209678, 0.023319649066299908, 0.00862922515959752, 0.15966545626765427, 0.9975177470324448, 0.7667867117538398, 0.04226480959432766, 0.3978014745893368]
      [0.19134970045873145, 0.47739681800224787, 0.7639644412685411, 0.9975177470324448, 0.6422727874038086, 0.6388079519464317, 0.09683230066428916, 0.3473861795807176]
      [0.4813343166055776, 0.7642636799092533, 0.23733729927123637, 0.7667867117538398, 0.6388079519464317, 0.7631389429131025, 0.9003153137806781, 0.6954859137262448]
      [0.5063442768371293, 0.8545120485746511, 0.6474221181599213, 0.04226480959432766, 0.09683230066428916, 0.9003153137806781, 0.6788474491255891, 0.50649745626266]
      [0.7976939280439258, 0.64167383494335, 0.3279445548632708, 0.3978014745893368, 0.3473861795807176, 0.6954859137262448, 0.50649745626266, 0.24520252207780557]

In the example above, "8" was chosen to be the size of the matrix to be generated. The above matrix generated is just
 one possible matrix generated, since the content of the matrix is generated randomly.  Calling this function
 again would (likely) produce a matrix with different randomly generated numbers inside.

**Implementation/Code:** The following is the code for gen_sym_matrix()


      import random
      
      def generate_sym_matrix():
          width = int(input("Please enter the width of the square matrix: "))
      
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0, width):
              for j in range(i, width):
                  value = random.random()
                  A[j][i] = value
                  A[i][j] = value
          return A
