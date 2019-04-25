# Software Manual (matrix_jacobian_gauss_seidel_compare.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_jacobian_gauss_seidel_compare.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compare the jacobian iteration to the gauss seidel iteration, by creating random
 matrices of various sizes, and then solving them.

**Input:** There are no inputs needed in this case. 

**Output:** This routine returns the results for solving various systems of equations using the Jacobian and Gauss Seidel iterations methods.
 The time it took to find the solution, as well as the number of iteratinos needed, are reported.

**Usage/Example:**

This method merly needs to be run in order to see the results:

      matrix_jacobian_gauss_seidel_compare()

Output from the line above:

      10x10 Jacobian:     Time: 0.008000612258911133, Iteration Count: 92
      10x10 Gauss Seidel: Time: 0.0010001659393310547, Iteration Count: 8
      50x50 Jacobian:     Time: 0.7600436210632324, Iteration Count: 551
      50x50 Gauss Seidel: Time: 0.011000633239746094, Iteration Count: 8
      100x100 Jacobian:     Time: 5.782330513000488, Iteration Count: 1089
      100x100 Gauss Seidel: Time: 0.04300236701965332, Iteration Count: 8
      200x200 Jacobian:     Time: 57.803305864334106, Iteration Count: 2529
      200x200 Gauss Seidel: Time: 0.18601059913635254, Iteration Count: 8
      500x500 Jacobian:     Time: 879.7503190040588, Iteration Count: 5883
      500x500 Gauss Seidel: Time: 1.3440766334533691, Iteration Count: 9
      1000x1000 Jacobian:     Time: 6203.067795038223, Iteration Count: 10000
      1000x1000 Gauss Seidel: Time: 5.479313611984253, Iteration Count: 9

Here we can see the results of solving random systems of equations using the Jacobian iteration and Gauss Seidel iteration.
We can clearly see that the Gauss Seidel iteration performs much better than the Jacobian iteration for all cases. When 
the matrix is just 10x10, the Gauss Seidel iteration is only 8 times faster than the Jacobian. But when the system gets as large 
as a 500x500 system, then the Gauss Seidel iteration outperforms the Jacobian iteration many orders of magnitudes faster.

**Implementation/Code:** The following is the code for matrix_jacobian_gauss_seidel_compare()

      import random
      import sys, os
      import time
      
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import matrix_solve_gauss_seidel, matrix_solve_jacobian, gen_sqr_diagdom_matrix
      
      
      def matrix_jacobian_gauss_seidel_compare():
          for i in [10,50,100,200,500]:
              matrix = gen_sqr_diagdom_matrix(i)
              vector = [1]*i
              starttime = time.time()
              solution,count = matrix_solve_jacobian(matrix, vector, 0.0001, 10000,getIterCount=True)
              print(str(i)+ "x" + str(i) + " Jacobian:     Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))
              starttime = time.time()
              solution, count = matrix_solve_gauss_seidel(matrix, vector, 0.0001, 10000,getIterCount=True)
              print(str(i)+ "x" + str(i) + " Gauss Seidel: Time: " + str(time.time() - starttime) + ", Iteration Count: " + str(count))
      
      matrix_jacobian_gauss_seidel_compare()
