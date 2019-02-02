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
  - Machine precision in single precision: [smaceps](Task1/smaceps.py).
  - Machine precision in double precision: [dmaceps](Task1/dmaceps.py). 
- Software Manual entries:
  - [smaceps](../software_manual/smaceps/smaceps.md)
  - [dmaceps](../software_manual/dmaceps/dmaceps.md)

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

1) I logged in to a computer at the Engineering Lab, an opened a command terminal<br>
2) I placed the 2 routines *smaceps.f* and *dmaceps.f* into a folder<br>
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
For this task, we were asked to run a routine (created by Joe Koebbe) to check how many cores are on the computer. 
I called the file provided *hello.f*, and in order to execute it, I created *hello.exe* with the command:

      gfortran -fopenmp hello.f -o hello

Then, I ran the compiled version of the code using the command:

      ./hello.exe

When run, the following output was produced:

      hello world from thread 4
      hello world from thread 2
      hello world from thread 6
      hello world from thread 5
      hello world from thread 1
      hello world from thread 7
      hello world from thread 3
      hello world from thread 0
      There are 8 threads!

This means that there are 8 cores on the computer.

- Code:
  - [hello.f](Task7/hello.f)
  - [hello.exe](Task7/hello.exe)

### Task 8
For this task, we were asked to read the three disaster articles at the site: http://www-users.math.umn.edu/~arnold//disasters/ <br>
and then write a brief paragraph on each of the disasters.

- **Disaster 1: The American Patriot Missile** <br> The American Patriot Missile was used to defend against an incoming Iraqi Scud missile. The American Patriot Missile was supposed to track the Iraqi Scud missile, but unfortunately it failed to do so because of a computation error. The missile counted time every 1/10 of a second using a 24 bit fixed point register, meaning that it only kept track of time using a variable with 24 digits. Since 1/10 in binary has an infinite binary expansion, that means that the binary value for 1/10 is only an approximation. Thus, 100 hours after the system had been booted up, the American Patriot Missile clock accumulated a significant error of 0.34 seconds off the actual time, causing the missle to fail.
- **Disaster 2: The Explosion of the Ariane 5** <br> The Ariane 5 rocket exploded just 40 seconds after lift-off. This un-intended explosion cost about 7 billion dollars in the development costs, and $500 million in the rocket itself. This error was caused due to a loss of guidance and altitude information. The rocket used a 16-bit signed integer to store a variable related in storing the horizontal speed of the rocket. A 16-bit signed integer can only store a value as high as 32767, which restricted the rockets guidance system. The failure occurred because the value that needed to be stored was greater than 32767.
- **Disaster 3: The sinking of the Sleipner A offshore platform** <br> The Sleipner A platform produces oil in gas in the North Sea. The concrete base structure for Sleipner A sprang a leak and sank, resulting in a loss of $700 million. The loss was due to insufficient strength in one of the walls that supported the structures. The insufficient strength was caused due to an inaccurate calculation that underestimated the strength of the shear stresses that the wall would need to support. If the finite element analysis has been done more carefully, then the flaw in the platform’s design would have been noticed earlier before construction.

### Task 9
For this task,Write a routine that will generate a random matrix of a given size. That is, input the number of rows 
and columns and output the matrix created by setting each entry in the matrix to a random value between zero and one.

- Code:
  - [gen_rand_matrix.py](Task9/gen_rand_matrix.py)
- Software Manual entry:
  - [gen_rand_matrix](../software_manual/gen_rand_matrix/gen_rand_matrix.md)

### Task 10
For this task, we were asked to search the internet for sites that discuss linear algebra packages for solving linear
 algebra problems. 

- **Site:** [NumPy](http://www.numpy.org/)<br>
NumPy is a python package for “scientific computing.” One of its main features is its powerful N dimensional array object, which is supported with many linear algebra functions. In addition to its linear algebra functionality, NumPy’s N dimensional array object and other features are also useful for generic data storage.
- **Site:** [LinearAlgebra 1.4.1](https://pypi.org/project/LinearAlgebra/)<br>
LinearAlgebra 1.4.1 is less sophisticated than NumPy, and just contains the main features of linear algebra computing. It contains a vector and matrix data type, as well as corresponding linear algebra functions.
- **Site:** [Plotly](https://plot.ly/python/user-guide/)<br>
Plotly is not linear algebra package, but I still believe that it may be helpful for class work. Plotly is a “data visualization toolbox”, or in other words, adds functionality to python mainly in graphing, plotting, and representing data.

