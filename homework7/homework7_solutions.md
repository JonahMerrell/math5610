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

| Matrix |    Jacobian        |     Jacobian       |Gaussian elimination|
|        |  Iteration Count   |        Time        |        Time        |
| 10x10  | 84				  | 0.009000  		   |      0.001000      |
| 50x50  | 493				  | 0.718041  		   |      0.027001      |
|100x100 | 1121				  | 6.035345  		   |      0.181010      |
|200x200 | 2215				  | 50.77390  	       |      1.425081      |
|500x500 | 6210			      | 940.8208  		   |      24.45239      |

For the system Ax = b, A is a random, diagonally-dominant matrix, and b is vector of just ones. The solution for the jacobian routine is calculated within a tolerance of 10E-4. Gaussian elimination found the solution much more efficiently and quickly than the jacobian iteration.

- Code:
  - [matrix_jacobian_gaussian_elimination_compare.py](Task1/matrix_jacobian_gaussian_elimination_compare.py)

### Task 2
For this task, we were asked to repeat the previous task using the Gauss-Seidel algorithm

| Matrix |    Guess Seidel    |     Guess Seidel   |Gaussian elimination|
|        |  Iteration Count   |        Time        |        Time        |
| 10x10  | 21				  | 0.002000  		   |      0.001000      |
| 50x50  | 21				  | 0.031001  		   |      0.026001      |
|100x100 | 21				  | 0.117006  		   |      0.180010      |
|200x200 | 22				  | 0.517029  	       |      1.429081      |
|500x500 | 22			      | 3.326190  		   |      24.00237      |


For the system Ax = b, A is a random, diagonally-dominant matrix, and b is vector of just ones. The solution for the gauss seidel routine is calculated within a tolerance of 10E-13.

From these results, we can see that at first, the Gauss Seidel iteration is slower than gaussian elimination. However, for matrices of larger sizes, the Gauss Seidel iteration becomes much faster than gaussian elimination. (the intersection happens with matrices between sizes 50 and 100).

- Code:
  - [matrix_guass_seidel_gaussian_elimination_compare.py](Task2/matrix_guass_seidel_gaussian_elimination_compare.py)

### Task 3
For this task, we were asked to implement the steepest descent method for solving linear systems of equations

- Code:
  - [matrix_solve_steepest_descent.py](Task3/matrix_solve_steepest_descent.py)
- Software Manual entry:
  - [matrix_solve_steepest_descent](../software_manual/matrix_solve_steepest_descent/matrix_solve_steepest_descent.md)

### Task 4
For this task, we were asked to try out your steepest descent method on Hilbert matrices of size 4, 8, 16, 32. Explain your results. 

| Hilbert Matrix | Descent Method Error |
| 4x4            | 0.009363		        |
| 8x8            | 0.019397		        |
| 16x16          | 0.028439		        |
| 32x32          | 0.038352	            |

After testing the steepest descent method on the hilbert matrix for vearious sizes, I found that after 10000 iterations, the hilbert matrices still hadnt converged,
with the exception of the 4x4 hilbert matrix, which converged after 190645 iterations to an accuracy of 1.7527E-13. After 10000 iterations, the steepest descent method 
still hadnt achieved precision within 10E-3 with the 8x8, 16x16, and 32x32 hilbert matrices

- Code:
  - [hilbert_matrix_steepest_descent_test.py](Task4/hilbert_matrix_steepest_descent_test.py)

### Task 5
For this task, we were asked to implement the Conjugate Gradient method.

- Code:
  - [matrix_solve_conjugate_gradient.py](Task5/matrix_solve_conjugate_gradient.py)
- Software Manual entry:
  - [matrix_solve_conjugate_gradient](../software_manual/matrix_solve_conjugate_gradient/matrix_solve_conjugate_gradient.md)

### Task 6
For this task, we were asked to try out the conjugate gradient method from the previous task on Hilbert matrices of order 4, 8, 16, and 32.

| Hilbert Matrix | Conjugate-Gradiant Error |
| 4x4            | 6.05644e-10		        |
| 8x8            | 3.47873e-05		        |
| 16x16          | 3.95861e-05		        |
| 32x32          | 4.16900e-05		        |

After testing the conjugate method for various precisions on the hilbert matrix for various sizes, I found that changing the tolerance of the iteration radicaly changed the result by far more than the tolerance change. I suspect that the hilbert matrix never converges. Despite running the program for e-10 precision, the 8x8,16x16, and 32x32 matrices had only achieved e-5.

Since testing for 10000 iterations didnt acheive e-10 precision, I tried testing the conjugate gradient method for 100000 iterations, to hopefully allow the computer more time to compute a solution to greater accuracy. Sadly, despite adding 10 times more iterations, the solutions for all 4 matrices I tested didnt increase in their precision.

I suspect doing additional iterations will not help these matrices converge any further.

- Code:
  - [hilbert_matrix_conjugate_gradient_test.py](Task6/hilbert_matrix_conjugate_gradient_test.py)

### Task 7
For this task, we were asked to do an internet search on the use of iterative methods for the solution of linear systems of equations that do not use preconditioning of the system. 

**Jacobian Iteration**
- https://en.wikipedia.org/wiki/Jacobi_method

**Gauss-Seidel iteration**
- https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method

**Modified Richardson iteration**
- https://en.wikipedia.org/wiki/Modified_Richardson_iteration

### Task 8
For this task, we were asked to look for internet sites that include descriptions of preconditioning of systems of equations.

Various pre-conditioning methods include:<br>
Linear preconditioning, Jacobi preconditioner, incomplete LU factorization, Spectral transformations

**Sources used:**
- http://www.mathcs.emory.edu/~benzi/Web_papers/survey.pdf 
- http://people.maths.ox.ac.uk/wathen/preconditioning.pdf 
- https://en.wikipedia.org/wiki/Preconditioner
- http://www.netlib.org/utk/people/JackDongarra/etemplates/node396.html

### Task 9
For this task, we were asked to compare results on symmetric positive definite linear systems of equations using Jacobi versus the conjugate gradient methods. 

| Matrix | Jacobian Iteration | Conjugate Gradient | Jacobian Iteration | Conjugate Gradient |
|        |  Iteration Count   | Iteration Count    |        Time        |        Time        |
| 10x10  | 116				  | 27  			   |     0.011000       |      0.002000      |
| 50x50  | 516				  | 10  			   |     0.734041       |      0.008000      |
|100x100 | 1167				  | 9  			       |     6.196354       |      0.026001      |
|200x200 | 2375				  | 9  			       |     54.31710       |      0.108006      |
|500x500 | 6170 		      | 8 			       |     947.2961       |      0.646037      |

For the system Ax = b, A is a random, diagonally-dominant matrix, and b is vector of just ones. The solution for the jacobian routine is calculated within a tolerance of 10E-4.The Conjugate Gradient method did much better than the jacobian iteration. The conjugate gradient method doesn't seem torequire more iterations as the size of the matrix got larger, and this made a huge difference for the large sized matrices such as the 500x500 matrix.

- Code:
  - [matrix_jacobian_conjugate_gradient_compare.py](Task9/matrix_jacobian_conjugate_gradient_compare.py)

### Task 10
For this task, we were asked to describe an algorithm for computing the solution of linear least squares systems using Jacobi iteration. Create an entry in your software manual for your algorihm and an example.

Given a system: Ax = b

Step 1: Convert Ax = b into normal equations:

A^t A x = A^t b

Step 2: Convert into a diagnally dominant system:

(A^t A + alpha I)x = A^t b + alpha I x

Step 3: Convert into a jacobian iteration:

((L + D + U)_AtA + alpha I)x = A^t b + alpha I x<bk>
(D_AtA + alpha I)x_k+1 = A^t b + alpha I x_k - (L + U)_AtA x_k

Step 4: Divide (invert) the matrix to solve for x_k+1

x_k+1 = A^t b + alpha I x_k - (L + U)_AtA x_k/(D_AtA + alpha I)

- Code:
  - [matrix_solve_jacobian_smart.py](Task10/matrix_solve_jacobian_smart.py)
- Software Manual entry:
  - [matrix_solve_jacobian_smart](../software_manual/matrix_solve_jacobian_smart/matrix_solve_jacobian_smart.md)
