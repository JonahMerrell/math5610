# Homework7<br>

## [Back](../)

- [x] [Task 1](#task-1)
- [x] [Task 2](#task-2)
- [x] [Task 3](#task-3)
- [x] [Task 4](#task-4)
- [x] [Task 5](#task-5)
- [x] [Task 6](#task-6)
- [x] [Task 7](#task-7)
- [x] [Task 8](#task-8)
- [x] [Task 9](#task-9)
- [x] [Task 10](#task-10)

### Task 1
For this task, we were asked to compare the results for the Jacobi iteration and Gaussian elimination on matrices that are diagonally dominant.

- Code:
  - [matrix_jacobian_gaussian_elimination_compare.py](Task1/matrix_jacobian_gaussian_elimination_compare.py)
- Software Manual entry:
  - [matrix_jacobian_gaussian_elimination_compare](../software_manual/matrix_jacobian_gaussian_elimination_compare/matrix_jacobian_gaussian_elimination_compare.md)

### Task 2
For this task, we were asked to repeat the previous task using the Gauss-Seidel algorithm

- Code:
  - [matrix_guass_seidel_gaussian_elimination_compare.py](Task2/matrix_guass_seidel_gaussian_elimination_compare.py)
  - [hilbert_matrix_QR_mod_test.py](Task2/hilbert_matrix_QR_mod_test.py)
- Software Manual entry:
  - [matrix_guass_seidel_gaussian_elimination_compare](../software_manual/matrix_guass_seidel_gaussian_elimination_compare/matrix_guass_seidel_gaussian_elimination_compare.md)

### Task 3
For this task, we were asked to implement the steepest descent method for solving linear systems of equations

- Code:
  - [matrix_solve_steepest_descent.py](Task3/matrix_solve_steepest_descent.py)
- Software Manual entry:
  - [matrix_solve_steepest_descent](../software_manual/matrix_solve_steepest_descent/matrix_solve_steepest_descent.md)

### Task 4
For this task, we were asked to try out your steepest descent method on Hilbert matrices of size 4, 8, 16, 32. Explain your results. 

- Code:
  - [hilbert_matrix_steepest_descent_test.py](Task4/hilbert_matrix_steepest_descent_test.py)
- Software Manual entry:
  - [hilbert_matrix_steepest_descent_test](../software_manual/hilbert_matrix_steepest_descent_test/hilbert_matrix_steepest_descent_test.md)

### Task 5
For this task, we were asked to implement the Conjugate Gradient method.

- Code:
  - [matrix_solve_conjugate_gradient.py](Task5/matrix_solve_conjugate_gradient.py)
- Software Manual entry:
  - [matrix_solve_conjugate_gradient](../software_manual/matrix_solve_conjugate_gradient/matrix_solve_conjugate_gradient.md)

### Task 6
For this task, we were asked to try out the conjugate gradient method from the previous task on Hilbert matrices of order 4, 8, 16, and 32.

- Code:
  - [hilbert_matrix_conjugate_gradient_test.py](Task6/hilbert_matrix_conjugate_gradient_test.py)
  - [matrix_solve_jacobian_test.py](Task6/matrix_solve_jacobian_test.py)
- Software Manual entry:
  - [hilbert_matrix_conjugate_gradient_test](../software_manual/hilbert_matrix_conjugate_gradient_test/hilbert_matrix_conjugate_gradient_test.md)

After performing the jacobian algorithm on a 1000x1000 matrix, it took 9696 iterations and 6943.37 seconds.

### Task 7
For this task, we were asked to do an internet search on the use of iterative methods for the solution of linear systems of equations. 






### Task 8
For this task, we were asked to look for internet sites that include descriptions of preconditioning of systems of equations.





### Task 9
For this task, we were asked to compare results on symmetric positive definite linear systems of equations using Jacobi versus the conjugate gradient methods. 

| Matrix | Jacobian Iteration | Conjugate Gradient | Jacobian Iteration | Conjugate Gradient |
| :----: |  Iteration Count   | Iteration Count    |        Time        |        Time        |
| 10x10  | 116				  | 27  			   |     0.011000       |      0.002000      |
| 50x50  | 516				  | 10  			   |     0.734041       |      0.008000      |
|100x100 | 1167				  | 9  			       |     6.196354       |      0.026001      |
|200x200 | 2375				  | 9  			       |     54.31710       |      0.108006      |
|		 |				      |   			       |                    |                    |

For the system Ax = b, A is a random, diagonally-dominant matrix, and b is vector of just ones. The solution for the jacobian routine is calculated within a tolerance of 10E-4.The Conjugate Gradient method did much better than the jacobian iteration. The conjugate gradient method doesn't seem torequire more iterations as the size of the matrix got larger, and this made a huge difference for the large sized matrices such as the 500x500 matrix.

- Code:
  - [matrix_jacobian_conjugate_gradient_compare.py](Task9/matrix_jacobian_conjugate_gradient_compare.py)
- Software Manual entry:
  - [matrix_jacobian_conjugate_gradient_compare](../software_manual/matrix_jacobian_conjugate_gradient_compare/matrix_jacobian_conjugate_gradient_compare.md)

### Task 10
For this task, we were asked to describe an algorithm for computing the solution of linear least squares systems using Jacobi iteration. Create an entry in your software manual for your algorihm and an example.

Given a system: Ax = b

Step 1: Convert Ax = b into normal equations:

A^t A x = A^t b

Step 2: Convert into a diagnally dominant system:

(A^t A + alpha I)x = A^t b + alpha I x

Step 3: Convert into a jacobian iteration:

((L + D + U)_AtA + alpha I)x = A^t b + alpha I x
(D_AtA + alpha I)x_k+1 = A^t b + alpha I x_k - (L + U)_AtA x_k

Step 4: Divide (invert) the matrix to solve for x_k+1

x_k+1 = A^t b + alpha I x_k - (L + U)_AtA x_k/(D_AtA + alpha I)

- Code:
  - [matrix_solve_jacobian_smart.py](Task10/matrix_solve_jacobian_smart.py)
- Software Manual entry:
  - [matrix_solve_jacobian_smart](../software_manual/matrix_solve_jacobian_smart/matrix_solve_jacobian_smart.md)
