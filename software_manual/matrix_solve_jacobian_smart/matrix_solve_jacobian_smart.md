# Software Manual (matrix_solve_jacobian_smart.py)

## [Back](../softwaremanual)

**Routine Name:**           matrix_solve_jacobian_smart.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will compute the solution of a square linear system of equations. (The system is of the form Ax = b)
The solution is calculated by the jacobian iteration. The intial guess (x_0) to start off our iteration is arbitrarily chosen to be the 0 vector.
This method is more robust than the traditional jacobian iteration, because this routine will solve the least sqaures system of the matrix A. 
Additionally, the resulting least sqaures system is modified to be garinteed to be diagonaly dominant (Which garintees that the jacobian iteration will converge).

**Input:** argument1: The matrix "A" in the system of linear equations Ax = b<br>
		   argument2: The vector "b" in the system of linear equations Ax = b<br>
           argument3: The tolerance used to determine when to stop iterating. (A number like 0.00001)<br>
		   argument4: The maximum iterations allowed while iterating.<br>
		   argument5: An optional parameter "getIterCount" set to false by default. (See output for details)
		   
**Output:** This routine returns the solution vector "x" to the system of linear equations. If "getIterCount" was
 set to true, then the routine will also output the number of iterations done to compute x.

**Usage/Example:**

Below shows an example of solving a system of linear equations of the form "Ax = b" using the routine "matrix_solve_jacobian_smart".
 Then the solution vector is printed. 

      matrix_example = [[5,10,2],[1,4,10],[2,1,5]]
      vector_example = [1,2,3]
      print(matrix_solve_jacobian_smart(matrix_example,vector_example,0.00001,10000))

Output from the lines above:

      [1.0214999324237763, -0.4677391485785134, 0.28494609326279147]

In the example above, the matrix representing "A" in the system "Ax = b" had a width of "3". The output vector "x"
 is the solution vector to the system, so that Ax = b.

**Implementation/Code:** The following is the code for matrix_solve_jacobian_smart()
      
      import sys, os
      sys.path.append(os.path.abspath('../../mylibrary'))
      from _mymodules import vector_scal_mult, vector_add, vector_2norm, matrix_mult, convert_vec_mat,matrix_transpose
      
      def matrix_solve_jacobian_smart(matrix,vector_b,tol,max_iter,getIterCount=False):
          matrix_mod = matrix_mult(matrix_transpose(matrix),matrix)
          vector_mod = convert_vec_mat(matrix_mult(matrix_transpose(matrix),convert_vec_mat(vector_b)))
          alpha = 0
          #This code finds the right valu for alpha to garintee that matrix_mod is diagonoly dominant.
          for i in range(len(matrix_mod)):
              tempVal = 0
              for j in range(len(matrix_mod[0])):
                  if j != i:
                      tempVal += matrix_mod[i][j]
                  else:
                      tempVal -= matrix_mod[i][j]
              alpha = max(alpha,tempVal)
          xnew = [0 for i in range(len(matrix_mod))]
          error = tol * 10
          count = 0
          while error > tol and count < max_iter:
              count += 1
              xold = xnew.copy()
              xnew = [(vector_mod[i]+alpha*xold[i]) for i in range(len(xold))]
              for i in range(len(matrix_mod)):
                  for j in range(i):
                      xnew[i] = xnew[i] - matrix_mod[i][j] * xold[j]
                  for j in range(i + 1, len(xnew)):
                      xnew[i] = xnew[i] - matrix_mod[i][j] * xold[j]
              for j in range(len(xnew)):
                  xnew[j] = xnew[j] / (matrix_mod[j][j] + alpha)
      
              error = vector_2norm(vector_add(convert_vec_mat(matrix_mult(matrix, convert_vec_mat(xnew))), vector_scal_mult(-1, vector_b)))
          if getIterCount == True:
              return xnew,count
          else:
              return xnew
