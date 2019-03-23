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
For this task, we were asked to implement a method that will return the approximate solution of a square linear system of equations where previous methods are not used. In my case, I used the least squares technique.

- Code:
  - [matrix_solve_least_square.py](Task1/matrix_solve_least_square.py)
  - [speed_test.py](Task1/speed_test.py)
- Software Manual entry:
  - [matrix_solve_least_square](../software_manual/matrix_solve_least_square/matrix_solve_least_square.md)

### Task 2
For this task, we were asked to implement a method that returns the LU-factorization of a square matrix.

- Code:
  - [matrix_LU_factor.py](Task2/matrix_LU_factor.py)
- Software Manual entry:
  - [matrix_LU_factor](../software_manual/matrix_LU_factor/matrix_LU_factor.md)

### Task 3
For this task, we were asked to solve a system of linear equations by performing LU factorization, followed with forward substitution and back substitution.

- Code:
  - [matrix_solve_LU.py](Task3/matrix_solve_LU.py)
- Software Manual entry:
  - [matrix_solve_LU](../software_manual/matrix_solve_LU/matrix_solve_LU.md)

### Task 4
For this task, we were asked to implement a method that will generate a symmetric, positive definite matrix.

- Code:
  - [gen_sym_posdef_matrix.py](Task4/gen_sym_posdef_matrix.py)
- Software Manual entry:
  - [gen_sym_posdef_matrix](../software_manual/gen_sym_posdef_matrix/gen_sym_posdef_matrix.md)

### Task 5
For this task, we were asked to implement a method that performs the Cholesky factorization method for square matrices

- Code:
  - [matrix_cholesky_fac.py](Task5/matrix_cholesky_fac.py)
- Software Manual entry:
  - [matrix_cholesky_fac](../software_manual/matrix_cholesky_fac/matrix_cholesky_fac.md)

### Task 6
For this task, we were asked to implement a method that will find the solution of a matrix using the least squares technique with normal equations.

- Code:
  - [matrix_solve_least_square_normal.py](Task6/matrix_solve_least_square_normal.py)
- Software Manual entry:
  - [matrix_solve_least_square_normal](../software_manual/matrix_solve_least_square_normal/matrix_solve_least_square_normal.md)

### Task 7
For this task, we were asked to implement a method that will find the solution of a matrix using a least squares technique with QR factorization

- Code:
  - [matrix_QR_factorization.py](Task7/matrix_QR_factorization.py)
- Software Manual entry:
  - [matrix_QR_factorization](../software_manual/matrix_QR_factorization/matrix_QR_factorization.md)

### Task 8
For this task, we were asked to implement a method that tests the QR factorization method on various hilbert matrices

- Code:
  - [hilbert_matrix_QR_test.py](Task8/hilbert_matrix_QR_test.py)
- Software Manual entry:
  - [hilbert_matrix_QR_test](../software_manual/hilbert_matrix_QR_test/hilbert_matrix_QR_test.md)

### Task 9
For this task, we were asked to write a routine that will generate a square diagonally dominant matrix.

- Code:
  - [gen_sqr_diagdom_matrix.py](Task9/gen_sqr_diagdom_matrix.py)
- Software Manual entry:
  - [gen_sqr_diagdom_matrix](../software_manual/gen_sqr_diagdom_matrix/gen_sqr_diagdom_matrix.md)

### Task 10
For this task, we were asked to search the internet for sites that discuss the use of direct methods for the approximate solution of linear systems of systems of equations.

There are various methods for computing the solution to a system of linear equations. Some of these methods include LU factorization, Gaussian Elimination and backward substitution, QR factorization, and the least squares method with Normal Equations.<br>
One of the advantages of iterative methods is the increased speed when it is sufficient to find an approximate solution to a low degree of accuracy. Direct methods for solving systems of linear equations cannot obtain a solution until the entire process is completed, so there is no notion of an inexact yet acceptable solution.<br>
Additionally, depending on the circumstances, we may have a good initial guess for the solution of a system of linear equations. Iterative methods can make good use of this decent initial guess to find an accurate solution quickly, while direct methods can not utilize an initial good guess at all. Additionally, direct methods can become significantly slower for large systems of equations compared to iterative methods, because the number of operations necessary for direct methods are of the order O(n3), while iterative methods are of the order O(n2). Also, error accumulation for direct methods grow significantly for large systems of equations. Another advantage of iterative methods is their memory usage, which is significantly less than a direct solver for the same sized problem.

**Sources used:**
- http://www.montefiore.ulg.ac.be/~geuzaine/INFO0939/hpc7.pdf
- https://math.stackexchange.com/questions/2590237/is-qr-decomposition-a-direct-linear-system-solving-method
- http://faculty.cse.tamu.edu/davis/publications_files/survey_tech_report.pdf
- https://math.stackexchange.com/questions/2462931/what-are-the-benefits-of-iterative-method-against-lu-decomposition
- https://people.eecs.berkeley.edu/~newton/Classes/EE219fa98/ee219a2_2/ee219a2_2.pdf
- https://www.comsol.com/blogs/solutions-linear-systems-equations-direct-iterative-solvers/
- https://ac.els-cdn.com/0898122188902623/1-s2.0-0898122188902623-main.pdf?_tid=7a54f0ee-6a4f-496f-93a7-3dda15b7612a&acdnat=1550794300_e042d57e90d5e3476b2a1421f3a13e6d

