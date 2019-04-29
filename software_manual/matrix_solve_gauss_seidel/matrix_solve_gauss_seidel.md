# Software Manual (matrix_solve_gauss_seidel.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_gauss_seidel.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by the gauss seidel iteration. The intial guess (x_0) to start off our iteration is arbitrarily chosen to be the 0 vector.

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b<br>
           argument3: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument4: The maximum iterations allowed while iterating.<br>
		   argument5: An optional parameter "getIterCount" set to false by default. (See output for details)
		   
**Output:** This routine returns the solution vector "x" to the system of linear equations. If "getIterCount" was
 set to true, then the routine will also output the number of iterations done to compute x.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_gauss_seidel".
 Then the solution vector is printed. 

      matrix_example = [[5,1,2],[1,4,1],[2,2,5]]
      vector_example = [1,2,3]
      print(matrix_solve_gauss_seidel(matrix_example,vector_example,0.00001,40))

Output from the lines above:

      [2.6226777706598146, -1.3299167200512425, -1.7258167841127303, -1.1672005124919766, 6.659192825112087]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "3". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_gauss_seidel()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_scal_mult,vector_add, vector_2norm, matrix_mult, convert_vec_mat
      
      def matrix_solve_gauss_seidel(matrix,vector_b,tol,max_iter,getIterCount=False):
          xnew = [0 for i in range(len(matrix))]
          error = tol * 10
          count = 0
          while error > tol and count < max_iter:
              #print(count) used for testing
              #print(error) used for testing
              count +=1
              xold = xnew.copy()
              xnew = vector_b.copy()
              for i in range(len(matrix)):
                  for j in range(i):
                      xnew[i] = xnew[i] - matrix[i][j]*xold[j]
                  for j in range(i+1,len(xnew)):
                      xnew[i] = xnew[i] - matrix[i][j]*xold[j]
                  xnew[i] = xnew[i] / matrix[i][i]
                  xold[i] = xnew[i]
              error = vector_2norm(vector_add(convert_vec_mat(matrix_mult(matrix,convert_vec_mat(xnew))),vector_scal_mult(-1,vector_b)))
          if getIterCount == True:
              return xnew,count
          else:
              return xnew
