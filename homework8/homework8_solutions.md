# Homework8<br>

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

### Task 1
For this task, we were asked to implement a code that will approximate the largest eigenvalue of a matrix using the Power Iteration algorithm. Test the code in the Hilbert matrix.

| Hilbert Matrix | Largest Eigenvalue |
| 4x4            | 1.5002142800562148 |
| 6x6            | 1.618899858921705  |
| 8x8            | 1.6959389968932237 |
| 10x10          | 1.7519196702597382 |

- Code:
  - [matrix_power_iteration.py](Task1/matrix_power_iteration.py)
  - [hilbert_matrix_power_iteration_test.py](Task1/hilbert_matrix_power_iteration_test.py)
- Software Manual entry:
  - [matrix_power_iteration](../software_manual/matrix_power_iteration/matrix_power_iteration.md)

### Task 2
For this task, we were asked to implement the Inverse Iteration method with shifting to find approximate eigenvalues of a matrix A. Find an eigenvalue less than the largest for the Hilbert matrix.

Smallest Eigenvalue for 4x4: 9.67023040226009e-05
Smallest Eigenvalue for 6x6: 1.0827994843804134e-07
Smallest Eigenvalue for 8x8: 1.1115389399118227e-10
Smallest Eigenvalue for 10x10: 1.0932741624186234e-13

| Hilbert Matrix | Smallest Eigenvalue    |
| 4x4            | 9.67023040226009e-05   |
| 6x6            | 1.0827994843804134e-07 |
| 8x8            | 1.1115389399118227e-10 |
| 10x10          | 1.0932741624186234e-13 |

- Code:
  - [matrix_inverse_power_iteration.py](Task2/matrix_inverse_power_iteration.py)
  - [hilbert_matrix_inverse_power_iteration_test.py](Task1/hilbert_matrix_inverse_power_iteration_test.py)
- Software Manual entry:
  - [matrix_inverse_power_iteration](../software_manual/matrix_inverse_power_iteration/matrix_inverse_power_iteration.md)

### Task 3
For this task, we were asked to compute an approximation of the condition in the 2-norm using your code to produce a largest and smallest eigenvalue of a matrix.

- Code:
  - [matrix_condition_number.py](Task3/matrix_condition_number.py)
- Software Manual entry:
  - [matrix_condition_number](../software_manual/matrix_condition_number/matrix_condition_number.md)

### Task 4
For this task, we were asked to test the code developed above to compute the condition number of the Hilbert matrix as the size of the matrix is increased.

| Hilbert Matrix | Condition Number   |
| 4x4            | 15513.73873892994  |
| 8x8            | 14951058.642686993 |
| 16x16          | 15257576104.851519 |
| 32x32          | 16024522763706.78  |

- Code:
  - [hilbert_matrix_condition_number_test.py](Task4/hilbert_matrix_condition_number_test.py)
- Software Manual entry:
  - [hilbert_matrix_condition_number_test](../software_manual/hilbert_matrix_condition_number_test/hilbert_matrix_condition_number_test.md)

### Task 5
For this task, we were asked to implement the Conjugate Gradient method, and then compute approximations of the smallest and largest eigenvalues. Next subdivide the interval containing the smallest and largest eigenvalues and use the points in the subdivision to shift and locate other eigenvalues. Discuss your results. 

The method can potentially find all of the eigenvectors for a matrix, as long as those eignvectors are "conviniently" placed. If the eigenvectors are clustered too close together, than the method will fail to identity all of them. Also, if a shift value is chosen too close to the exact middle of 2 eigenvalues, then the method's current max iteration count may not be enough to allow convergence, even if it outherwise would. Finally, I found that when a matrix has 2 eigenvalues of equal magnitude but opposite signs, then it would often only be able to converge on of them.

- Code:
  - [matrix_find_eigenvalues.py](Task5/matrix_find_eigenvalues.py)
- Software Manual entry:
  - [matrix_find_eigenvalues](../software_manual/matrix_find_eigenvalues/matrix_find_eigenvalues.md)

### Task 6
For this task, we were asked to Implement the Raleigh Quotient algorithm for computing approximations for eigenvalues of a matrix. Test the code on a Hilbert matrix.

| Hilbert Matrix | Eigenvalue         |
| 4x4            | 1.5002142800592426 |
| 8x8            | 1.6188998589243389 |
| 16x16          | 1.69593899692195   |
| 32x32          | 1.7519196702651771 |

- Code:
  - [matrix_rayleigh_quotient_iteration.py](Task6/matrix_rayleigh_quotient_iteration.py)
  - [hilbert_matrix_rayleigh_quotient_iteration_test.py](Task6/hilbert_matrix_rayleigh_quotient_iteration_test.py)
- Software Manual entry:
  - [matrix_rayleigh_quotient_iteration](../software_manual/matrix_rayleigh_quotient_iteration/matrix_rayleigh_quotient_iteration.md)

### Task 7
For this task, we were asked use the Rayleigh Quotient algorthm to compute an approximation for the condition of the matrix. Test your code on a Hilbert matrix

This algorithm for computing an aproximation for the condition number of a matrix function very similarly to the
 "matrix_condition_number" routine made for task 3. The "matrix_condition_number" algorithm uses the power iteration
 method to compute the largest eigenvalue, while this method uses the Rayleigh Quotient algorithm to compute the largest
 eigenvalue. Since a starting eigenvalue can not be specified for the Rayleigh Quotient algorithm (Since this algorthm
 choses the shifting value for you during run-time), this means that I was not able to use this algorthm to substitute
 the Inverse Iteration method instead (which is used to compute the smallest eigenvalue). When tested on a 10x10 hilbert matrix,
 the routine accuratly produced the same results as before: 16024243403150.434. (previously calcualted from task 4)

- Code:
  - [matrix_condition_number_rayleigh_quotient.py](Task7/matrix_condition_number_rayleigh_quotient.py)
- Software Manual entry:
  - [matrix_condition_number_rayleigh_quotient](../software_manual/matrix_condition_number_rayleigh_quotient/matrix_condition_number_rayleigh_quotient.md)

### Task 8
For this task, we were asked to look for internet sites that estimate the condition number of a matrix.

There are many ways to approximate the condition number of a matrix. The official formula is \|\|A\|\|*\|\|A^-1\|\|, however computing this formula is not generally used since computing \|\|A^-1\|\| would essentially already solve the problem.<br>
One method for approximating the condition number of a matrix is to compute the largest and smallest eigenvector of A, and then compute |λmax|/| λmin|.<br>
Another method used to approximate the condition number is simply to approximate the norms of A and A^-1, and then use these estimates directly in the actual formula \|\|A\|\|*\|\|A^-1\|\|. A common method used to approximate the norms of A is b singular value decomposition.<br>
A third method sometimes used is based on hager’s method. This method can estimate the 1-norm for the matrix A and A^-1, and once again these estimates directly used in the actual formula \|\|A\|\|*\|\|A^-1\|\|.

**Sources used:**

- https://en.wikipedia.org/wiki/Condition_number
- http://www.alglib.net/matrixops/rcond.php
- https://cseweb.ucsd.edu/classes/fa04/cse252c/sakumar.pdf
- https://en.wikipedia.org/wiki/Singular_value_decomposition
- https://www.cs.cmu.edu/~venkatg/teaching/CStheory-infoage/book-chapter-4.pdf
- http://www.cs.utexas.edu/~henear/works/2016posterprint.pdf

### Task 9
For this task, we were asked to Compare the Inverse Iteration Algorithm and the Rayleigh Quotient Algorithm in terms of the amount of time needed to compute an eigenvalue.

| Matrix | Inverse Power      | Rayleigh Quotient  | Inverse Power      | Rayleigh Quotient    |
|        |  Iteration Count   | Iteration Count    |        Time        |        Time          |
| 10x10  | 72				  | 6  			       | 0.0390024185180664 | 0.003000020980834961 |
| 50x50  | 46				  | 5  			       | 0.9680554866790771 | 0.10900616645812988  |
|100x100 | 150				  | 10000  			   | 21.25821566581726  | 1437.0341939926147   |
|200x200 | 248				  | 5  			       | 265.8172039985657  | 5.532316446304321    |

From these results, we can see that the rayleigh quotient algorithm is faster at calculating an eigen value than the inverse power method.
However, we can see from the table above that the rayleight quotient method may not always converge. When tested on a 100x100 matrix above,
we can see that the matrix didnt converge, until it reached its iteration max at 10000.

- Code:
  - [matrix_inverse_iteration_rayleigh_quotient_compare.py](Task9/matrix_inverse_iteration_rayleigh_quotient_compare.py)
- Software Manual entry:
  - [matrix_inverse_iteration_rayleigh_quotient_compare](../software_manual/matrix_inverse_iteration_rayleigh_quotient_compare/matrix_inverse_iteration_rayleigh_quotient_compare.md)