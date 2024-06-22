# 361 - HW2

2022-2023 Spring Semester

This is my multi-thread program that asks a user for two vectors. It then uses two threads, to add and subtract the first vector and the second vector. One thread is used for addition, and the other is used for subtraction. Once the threads' tasks are done, then the sum and difference vectors will be displayed, as well as the total completion time. 

## Compilation
1. Open VScode, or use command line.
2. Change the directory to that of which this project folder is saved to.
3. Type the following into the command line: 
    * python main.py
4. You'll then be asked to type in 2 vectors with the following prompts: 
    * Input 3 integers (i.e x y z) then press ENTER: 
      * After typing the 3 integers, and pressing ENTER...
    * Input 3 integers (i.e x y z) then press ENTER: 
      * After pressing ENTER, the program will run correctly
5. Make sure to space out each dimension of the vector like so:
    * x y z     --> Example: 1 2 3

---------------------------------------------------------------------------------------------------------------------------

## Compliation Example
"*ENTER" is expressed as pressing ENTER on the keyboard

```
python main.py      *ENTER
Input 3 integers (i.e x y z) then press ENTER: 6 7 8    *ENTER
Input 3 integers (i.e x y z) then press ENTER: 1 2 3    *ENTER
Sum Vector: 7 9 11
Difference Vector: 5 5 5
It took 7.35 second(s) to copmlete.
```