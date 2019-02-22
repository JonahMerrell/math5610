# Software Manual (matrix_ref.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_ref.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will perform elementary row operations on a matrix to take the matrix to row echelon form

**Input:** argument1: The matrix to be find the row echelon form of.<br>

**Output:** This routine returns a matrix resulting from changing the input matrix given into row echelon form.

**Usage/Example:**

Below shows an example of reducing a matrix to row echelon form using the routine "matrix_ref" (one row is printed at a time, for
 readabilities sake).

      matrix = [[6,5,4,3,2],[8,9,8,3,5],[1,3,4,6,8],[5,2,7,4,5],[7,3,8,5,8]]
      matrix_new = matrix_ref(matrix)
      for i in range(0,len(matrix)):
          print(matrix_new[i])

Output from the lines above:

      [1.0, 0.8333333333333331, 0.6666666666666665, 0.5, 0.33333333333333326]
      [0.0, 1.0, 1.1428571428571426, -0.4285714285714284, 0.9999999999999998]
      [0.0, 0.0, 1.0, 7.499999999999999, 6.416666666666666]
      [-0.0, -0.0, -0.0, 1.0, 0.7454212454212452]
      [0.0, 0.0, 0.0, 2.4853064300129014e-15, 1.0]

The above matrix printed is the original matrix reduced to row echelon form.

**Implementation/Code:** The following is the code for matrix_ref()

      import copy
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_add, vector_scal_mult

      def matrix_ref(matrix):
          n = len(matrix)
          #m = len(matrix[0])
          solution = copy.deepcopy(matrix)
          for i in range(0,n):
              for j in range(i+1, n):
                  if solution[i][i] !=0:
                      solution[j] = vector_add(solution[j],vector_scal_mult(-solution[j][i]/solution[i][i],solution[i]))
              solution[i] = vector_scal_mult(1/solution[i][i],solution[i])
          return solution
