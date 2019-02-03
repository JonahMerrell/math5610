# Homework2<br>

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
For this task, we were asked to email the link to your repository and table of contents for your completed homework tasks.

- Link to my github pages website: [https://jonahmerrell.github.io/math5610](https://jonahmerrell.github.io/math5610)

### Task 2
For this task, we were asked to implement a method/routine that computes and returns the absolute error in the approximation of a number x by another number y.

- Code:
  - [abs_error.py](Task2/abs_error.py)
- Software Manual entry:
  - [abs_error](../software_manual/abs_error/abs_error.md)

### Task 3
For this task, we were asked to implement a method/routine that computes and returns the relative error in the approximation of a number x by another number y.

- Code:
  - [rel_error.py](Task3/rel_error.py)
- Software Manual entry:
  - [rel_error](../software_manual/rel_error/rel_error.md)
  
### Task 4
For this task, we were asked to implement a method that will add two vectors of the same length.

- Code:
  - [vector_add.py](Task4/vector_add.py)
- Software Manual entry:
  - [vector_add](../software_manual/vector_add/vector_add.md)

### Task 5
For this task, we were asked to implement a method that will return a scalar multiple of a given vector. The method should require a vector and number for the operation.

- Code:
  - [vector_scal_mult.py](Task5/vector_scal_mult.py)
- Software Manual entry:
  - [vector_scal_mult](../software_manual/vector_scal_mult/vector_scal_mult.md)

### Task 6
For this task, we were asked to implement a method that will compute the 2-norm of an arbitrary vector will real number entries.

- Code:
  - [vector_2norm.py](Task6/vector_2norm.py)
- Software Manual entry:
  - [vector_2norm](../software_manual/vector_2norm/vector_2norm.md)

### Task 7
For this task, we were asked to implement a method that will compute the 1-norm of an arbitrary vector will real number entries.

- Code:
  - [vector_1norm.py](Task7/vector_1norm.py)
- Software Manual entry:
  - [vector_1norm](../software_manual/vector_1norm/vector_1norm.md)

### Task 8
For this task, we were asked to implement a method that will compute the ∞-norm of an arbitrary vector will real number entries.

- Code:
  - [norm_inf_vector.py](Task8/norm_inf_vector.py)
- Software Manual entry:
  - [norm_inf_vector](../software_manual/norm_inf_vector/norm_inf_vector.md)

### Task 9
For this task, we were asked to write a routine that will generate a symmetric matrix that has real values in all entries of the matrix.

- Code:
  - [gen_sym_matrix.py](Task9/gen_sym_matrix.py)
- Software Manual entry:
  - [gen_sym_matrix](../software_manual/gen_sym_matrix/gen_sym_matrix.md)

### Task 10
- For this task, we were asked to search the internet for sites that discuss matrix norms, and write a brief summary of what you find.

A matrix norm is a way of measuring the numerical “size” or “magnitude” of a matrix. There is no exact formula for calculating a matrix norm, since all that is needed for a matrix norm formula to be valid is to for the formula to have the following properties: <br>
llαAll = lαl llAll <br>
llA + Bll = llAll + llBll <br>
llAll >= 0 <br>
llAll = 0 iff A = 0m,n <br>
Thus, there can be many candidates for valid matrix norms. An induced matrix norm is a norm formula based off how much larger a vector gets when the matrix is operated on the vector. (The matrix acts as a linear operator on the vector). For example, 3 vector norms include the 1-norm, 2-norm, and infinity-norm, and each one of these vector-norms has a corresponding induced matrix norm. 

**Sources used:**
- https://en.wikipedia.org/wiki/Matrix_norm
- https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-241j-dynamic-systems-and-control-spring-2011/readings/MIT6_241JS11_chap04.pdf
- https://nptel.ac.in/courses/122104019/numerical-analysis/kadalbajoo/lec1/fnode3.html



