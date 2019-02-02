# Homework1<br>

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
For this task, we were asked to create two routines. One routine would measure the machine
precision of single precision arithmetic, and the other routine would measure the machine
precision of double precision arithmetic.

- Code:
  - Machine precision in [single precision](Task1/smaceps.py).
  - Machine precision in [double precision](Task1/dmaceps.py). 
- Software Manual entries:
  - [single precision](../software_manual/smaceps/smaceps.md)
  - [double precision](../software_manual/dmaceps/dmaceps.md)

### Task 2
For this task, we were asked to create a repository at github.com with the name username/math5610.

- Link to my github Repository: [https://github.com/JonahMerrell/math5610](https://github.com/JonahMerrell/math5610)

### Task 3
For this task, we were asked to create a repository at github pages.

- Link to my github pages website: [https://jonahmerrell.github.io/math5610](https://jonahmerrell.github.io/math5610)

### Task 4
For this task, we were asked to create a software manual, to be used for all of the programs we make throughout the class.

- Link to my Software Manual: [https://jonahmerrell.github.io/math5610/software_manual/softwaremanual](https://jonahmerrell.github.io/math5610/software_manual/softwaremanual)

### Task 5
For this task, we were asked to create a table of contents for the homework tasks. In my case, my table of contents is
set up to be the homepage for my github pages website.

- Link to my Table of Contents: [https://jonahmerrell.github.io/math5610](https://jonahmerrell.github.io/math5610)

### Task 6
For this task, we were asked to create a shared library of our code. The 2 routines created during task1 were used as
the first 2 files in the shared library. I used the fortran version of the two routines provided by Joe Koebbe for this task.
The 2 files are called *smaceps.f* and *dmaceps.f* (See below for all files created/used during this task). In order to
create the shared library, I did the following:

1) I logged in to a computer at the Engineering Lab, an opened a command terminal
2) I placed the 2 routines *smaceps.f* and *dmaceps.f* into a folder
3) I compiled the 2 routines into object modules *smaceps.o* and *dmaceps.o*, using the following command:

      gfortran -c *.f

4) I created a shared library *mylib.a* from the ".o" files I just created using the command

      ar rcv mylib.a *.o

5) In order to test that my shared library was functioning properly, I created a driver routine called "test.f" that 
would run the two routines from the shared library. To execute my *test.f* file, I created *test.exe* with the command:

      gfortran test.f mylib.a -o test.exe

6) Finally, I ran *test.exe* to verify that my shared library is working, using the command:

      ./test.exe

- Code:
  - [dmaceps.f](Task6/dmaceps.f)
  - [smaceps.f](Task6/smaceps.f)
  - [dmaceps.o](Task6/dmaceps.o)
  - [smaceps.o](Task6/smaceps.o)
  - [mylib.a](Task6/mylib.a)
  - [test.f](Task6/test.f)
  - [test.exe](Task6/test.exe)   
  - [mylib](Task6/mylib)



### Task 7
- [Answer.pdf](Task7/Answer.pdf)
- [hello.exe](Task7/hello.exe)
- [hello.f](Task7/hello.f)

### Task 8
- [Task8_paragraphs.pdf](Task8/Answer.pdf)

### Task 9
- [gen_rand_matrix.py](Task9/gen_rand_matrix.py)

### Task 10
- [Linear_Algebra_Packages.pdf](Task10/Linear_Algebra_Packages.pdf)
