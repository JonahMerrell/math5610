# Homework5<br>

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
For this task, we were asked to implement a method that will compute the solution of a square linear system of equations using the QR-factorization of the matrix.

- Code:
  - [matrix_solve_QR_factorization.py](Task1/matrix_solve_QR_factorization.py)
- Software Manual entry:
  - [matrix_solve_QR_factorization](../software_manual/matrix_solve_QR_factorization/matrix_solve_QR_factorization.md)

### Task 2
For this task, we were asked to create another version of the QR-factorization algorithm using the Modified Gram-Schmidt process. 

- Code:
  - [matrix_QR_factorization_mod.py](Task2/matrix_QR_factorization_mod.py)
  - [hilbert_matrix_QR_mod_test.py](Task2/hilbert_matrix_QR_mod_test.py)
- Software Manual entry:
  - [matrix_QR_factorization_mod](../software_manual/matrix_QR_factorization_mod/matrix_QR_factorization_mod.md)

### Task 3
For this task, we were asked to create a third version of the QR-factorization algorithm using Householder Transformations.

- Code:
  - [matrix_QR_factorization_householder.py](Task3/matrix_QR_factorization_householder.py)
- Software Manual entry:
  - [matrix_QR_factorization_householder](../software_manual/matrix_QR_factorization_householder/matrix_QR_factorization_householder.md)

### Task 4
For this task, we were asked to solve the least squares problem using QR factorization with the Gram-Schmidt algorithm.

- Code:
  - [matrix_solve_least_squares_QR.py](Task4/matrix_solve_least_squares_QR.py)
- Software Manual entry:
  - [matrix_solve_least_squares_QR](../software_manual/matrix_solve_least_squares_QR/matrix_solve_least_squares_QR.md)

### Task 5
For this task, we were asked to solve the least squares problem. In my case, I used Householder matrices

- Code:
  - [matrix_solve_least_squares_QR_householder.py](Task5/matrix_solve_least_squares_QR_householder.py)
- Software Manual entry:
  - [matrix_solve_least_squares_QR_householder](../software_manual/matrix_solve_least_squares_QR_householder/matrix_solve_least_squares_QR_householder.md)

### Task 6
For this task, we were asked to implement the Jacobi Iteration algorithm.

- Code:
  - [matrix_solve_jacobian.py](Task6/matrix_solve_jacobian.py)
  - [matrix_solve_jacobian_test.py](Task6/matrix_solve_jacobian_test.py)
- Software Manual entry:
  - [matrix_solve_jacobian](../software_manual/matrix_solve_jacobian/matrix_solve_jacobian.md)

### Task 7
For this task, we were asked to implement the Gauss-Seidel algorithm.

- Code:
  - [matrix_solve_gauss_seidel.py](Task7/matrix_solve_gauss_seidel.py)
  - [matrix_solve_gauss_seidel_test.py](Task7/matrix_solve_gauss_seidel_test.py)
- Software Manual entry:
  - [matrix_solve_gauss_seidel](../software_manual/matrix_solve_gauss_seidel/matrix_solve_gauss_seidel.md)

### Task 8
For this task, we were asked to compare the Jacobi and Gauss-Seidel in terms of the number of iterations needed to converge to a given tolerance.

- Code:
  - [matrix_jacobian_gauss_seidel_compare.py](Task8/matrix_jacobian_gauss_seidel_compare.py)
- Software Manual entry:
  - [matrix_jacobian_gauss_seidel_compare](../software_manual/matrix_jacobian_gauss_seidel_compare/matrix_jacobian_gauss_seidel_compare.md)

### Task 9
For this task, we were asked to do an internet search for pages that discuss the difference between the solution of the least squares problem using the normal equations and the solution via QR factorization of the matrix.

QR decomposition yields a better result than the normal equations, because although QR is more computationally expensive (when m >> n), it is more robust.<br>
This is because normal equations compute the least square solution to an overdetermined system of equations by computing A*AT. As far as the condition number of the system is concerned, this is essentially computing A2, which means that the condition number is squared. As a result, this causes the condition number of the problem to increase dramatically.<br>
Thus, QR decomposition yields better results with less well-conditioned matrices.

**Sources used:**
https://www.cs.cornell.edu/~bindel/class/cs3220-s12/notes/lec10.pdf
https://www.quora.com/Is-it-better-to-do-QR-Cholesky-or-SVD-for-solving-least-squares-estimate-and-why
https://math.stackexchange.com/questions/2339079/qr-factorization-for-solving-least-squares

### Task 10
For this task, we were asked to do an internet search for sites that discuss the stability of various algorithms used in computing the QR factorization of both rectangular and square matrices.

To compute the QR factorization of the matrix, you can use the Gram-Schmidt process, householder reflection, or Givens rotations.<br>
The Gram-Schmidt process is considered the least stable of the three methods, since the orthogonalization itself is prone to numerical error. This is because when implemented on a computer, rounding errors cause the orthogonal vectors to be not quite orthogonal. The non-orthogonality accumulates error over time. The householder reflection is considered more numericaly stable and more efficient than the Gram-Schmidt process (And even Givens rotations) to compute the QR factorization. The Householder method computes the Q-factor as a product of accurate Householder reflections, which doesn’t accumulate error over time. Givens rotations are considered more efficient and parrelisable than the householder reflection, although Givens rotations are more difficult to implement, and slower than Householder refelctions.

**Sources used:**
- https://en.wikipedia.org/wiki/QR_decomposition
- https://www-old.math.gatech.edu/academic/courses/core/math2601/Web-notes/3num.pdf
- http://iacs-courses.seas.harvard.edu/courses/am205/fall13/AM205_unit_2_chapter_3.pdf
- https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process#Numerical_stability
- https://www-old.math.gatech.edu/academic/courses/core/math2601/Web-notes/3num.pdf

