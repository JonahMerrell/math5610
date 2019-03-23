# Homework4<br>

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
For this task, we were asked to implement a method that returns the absolute error in the approximation of one vector by another when the 2-norm is used.

- Code:
  - [matrix_scal_mult.py](Task1/matrix_scal_mult.py)
- Software Manual entry:
  - [matrix_scal_mult](../software_manual/matrix_scal_mult/matrix_scal_mult.md)

### Task 2
For this task, we were asked to implement a method that returns the absolute error in the approximation of one vector by another when the 1-norm is used

- Code:
  - [matrix_add.py](Task2/matrix_add.py)
- Software Manual entry:
  - [matrix_add](../software_manual/matrix_add/matrix_add.md)

### Task 3
For this task, we were asked to implement a method that returns the absolute error in the approximation of one vector by another when the ∞-norm is used

- Code:
  - [matrix_outer.py](Task3/matrix_outer.py)
- Software Manual entry:
  - [matrix_outer](../software_manual/matrix_outer/matrix_outer.md)

### Task 4
For this task, we were asked to implement a method that returns the 1-matrix norm of a given square matrix.

- Code:
  - [matrix_solve_diagonal.py](Task4/matrix_solve_diagonal.py)
- Software Manual entry:
  - [matrix_solve_diagonal](../software_manual/matrix_solve_diagonal/matrix_solve_diagonal.md)

### Task 5
For this task, we were asked to implement a method that returns the ∞-norm of a given square matrix.

- Code:
  - [matrix_solve_upper_tri.py](Task5/matrix_solve_upper_tri.py)
- Software Manual entry:
  - [matrix_solve_upper_tri](../software_manual/matrix_solve_upper_tri/matrix_solve_upper_tri.md)

### Task 6
For this task, we were asked to implement a method that returns the dot produce of two vectors of the same length.

- Code:
  - [matrix_solve_lower_tri.py](Task6/matrix_solve_lower_tri.py)
- Software Manual entry:
  - [matrix_solve_lower_tri](../software_manual/matrix_solve_lower_tri/matrix_solve_lower_tri.md)

### Task 7
For this task, we were asked to implement a method that returns the cross-product of two vectors of length three.

- Code:
  - [matrix_ref.py](Task7/matrix_ref.py)
- Software Manual entry:
  - [matrix_ref](../software_manual/matrix_ref/matrix_ref.md)

### Task 8
For this task, we were asked to implement a method that returns the product of two matrices with an equal inner dimension.

- Code:
  - [matrix_solve.py](Task8/matrix_solve.py)
- Software Manual entry:
  - [matrix_solve](../software_manual/matrix_solve/matrix_solve.md)

### Task 9
For this task, we were asked to write a routine that will generate a diagonally dominant matrix that has real values in all entries of the matrix.

- Code:
  - [gen_diagdom_sym_matrix.py](Task9/gen_diagdom_sym_matrix.py)
- Software Manual entry:
  - [gen_diagdom_sym_matrix](../software_manual/gen_diagdom_sym_matrix/gen_diagdom_sym_matrix.md)

### Task 10
For this task, we were asked to search the internet for sites that discuss parallel algorithms for matrix-vector multiplication and matrix-matrix multiplication..

A parallel algorithm for matrix-vector/matrix-matrix multiplication refers to performing matrix operations on a computer, and achieving optimal computation speeds by utilizing parallel processing. Since a computer often has multiple processers, then the various tasks necessary to perform a matrix operation can be distributed among the multiple processors of the computer system. This can be done by partitioning the data into stripes (columns/rows), or into rectangular fragments (blocks).<br> 
Parallel processing can be difficult to program, because sending or receiving information from one processer to another takes up time, in addition to performing a calculation. Properly organizing a “network” of processers to work together to solve pieces of a problem and then assemble the pieces together can be difficult to implement, which is why partitioning data into simple “stripes” or “blocks” is the most commonly used approach.

**Sources used:**
- http://www.hpcc.unn.ru/mskurs/ENG/DOC/pp07.pdf
- https://ac.els-cdn.com/0898122188902623/1-s2.0-0898122188902623-main.pdf?_tid=7a54f0ee-6a4f-496f-93a7-3dda15b7612a&acdnat=1550794300_e042d57e90d5e3476b2a1421f3a13e6d

