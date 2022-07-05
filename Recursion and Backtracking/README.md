# **Lab: Recursion and Backtracking**

This document defines the lab for [&quot;Algorithms with Python&quot; course @Software University](https://softuni.bg/opencourses/algorithms-with-python)&quot;.

Please submit your solutions (source code) of all below-described problems in [Judge](https://judge.softuni.org/Contests/3459/).

## 1. Recursive Array Sum

Write a program that finds the sum of all elements in an integer array. Use **recursion**.

**Note** : In practice, this recursion should not be used here (instead use an **iterative solution** ), this is just an exercise.

### Examples

| **Input** | **Output** |
| --- | --- |
| 1 2 3 4 | 10 |
| -1 0 1 | 0 |


Write a **recursive** method. It will take as arguments the **input array** and an **index**.

- The method should return the **current element** + the **sum of all next elements** (obtained by recursively calling it):


- The recursion should stop when there are no more elements in the array:


- This is how the complete solution should look:



## 2. Recursive Factorial

Write a program that calculates the recursively factorial of a given number.

**NOTE** : In practice, this recursion should not be used here (instead use an **iterative solution** ).

### Examples

| **Input** | **Output** |
| --- | --- |
| 5 | 120 |
| 10 | 3628800 |

### Hints

Write a **recursive** method. It will take as arguments an integer number.

- The method should return the **current element** \* the **result of calculating the factorial of current element - 1** (obtained by recursively calling it).
- The recursion should stop when the last element is reached.


## 3. Recursive Drawing

Write a program that draws the figure below depending on **n**.

### Examples
![image info](./images/Drawing.png)

1.
## Generating 0/1 Vectors

Generate all **n** -bit vectors of **0** and **1** in **lexicographic order**.

### Examples

| **Input** | **Output** |
| --- | --- |
| 3 | 000<br/>001<br/>010<br/>011<br/>100<br/>101<br/>110<br/>111 |


- The method should receive as parameters the array which will be our vector and an index.
- The bottom of the recursion should be when the index is outside of the vector.
- To generate all combinations, create a for loop with a recursive call:



## 5. Find All Paths in a Labyrinth

You are given a labyrinth. Your goal is to find all paths from the start (cell 0, 0) to the exit, marked with &#39;e&#39;.

- Empty cells are marked with a dash &#39;-&#39;.
- Walls are marked with a star &#39;\*&#39;.

On the first line, you will receive the dimensions of the labyrinth. Next, you will receive the actual labyrinth.

The order of the paths does not matter.

**Examples**

| **Input** | **Output** |
| --- | --- |
| 3<br/>3<br/>---<br/>-\*-<br/>--e | RRDD<br/>DDRR |
| 3<br/>5-\*\*-e<br/>-----<br/>\*\*\*\*\* | DRRRRU<br/>DRRRUR |

**Hints**

- Create methods for reading and finding all paths in the labyrinth.


- Finding all paths should be recursive.


- Implement all helper methods that are present in the code above.

## 6. Queens Puzzle

In this lab, we will implement a recursive algorithm to solve the **&quot;8 Queens&quot; puzzle**. Our goal is to write a program to **find all possible placements of 8 chess queens** on a chessboard so that no two queens can attack each other (on a row, column, or diagonal).

### Examples

| **Input** | **Output** |
| --- | --- |
| _(no input)_ | <br/>* - - - - - - -<br/>- - - - \* - - -<br/> - - - - - - - \* <br/>- - - - - \* - - <br/>- - \* - - - - -<br/> - - - - - - \* - <br/>- \* - - - - - -<br/> - - - \* - - - -
|


(90 solutions more)

### Hints

#### Learn about the &quot;8 Queens&quot; Puzzle

Learn about the &quot;8 Queens&quot; puzzle, e.g. from Wikipedia: [http://en.wikipedia.org/wiki/Eight\_queens\_puzzle](http://en.wikipedia.org/wiki/Eight_queens_puzzle).

#### Define a Data Structure to Hold the Chessboard

First, let&#39;s define a data structure to hold the **chessboard**. It should consist of 8 x 8 cells, each either occupied by a queen or empty. Let&#39;s also define the size of the chessboard as a constant:

#### Define a Data Structure to Hold the Attacked Positions

We need to **hold the attacked positions** in some data structure. At any moment during the execution of the program, we need to know **whether a certain**** position ****{row, col} is under attack** by a queen or not.

There are many ways to **store the attacked positions** :

- By keeping **all currently placed queens** and checking whether the new position conflicts with some of them.
- By keeping a **matrix of all attacked positions** and checking the new position directly in it. This will be complex to maintain because the matrix should change many positions after each queen placement/removal.
- By keeping **sets of all attacked rows, columns, and diagonals**. Let&#39;s try this idea:

The above definitions have the following assumptions:

- **The Rows** are 8, numbered from 0 to 7.
- **The Columns** are 8, numbered from 0 to 7.
- The **left diagonals** are 15, numbered from -7 to 7. We can use the following formula to calculate the left diagonal number by row and column: **left\_diag**** = ****col**** - ****row**.
- The **right diagonals** are 15, numbered from 0 to 14 by the formula: **right\_diag**** = ****col**** + ****row**.

Let&#39;s take as an **example** the following chessboard with 8 queens placed on it at the following positions:

- {0, 0}; {1, 6}; {2, 4}; {3, 7}; {4, 1}; {5, 3}; {6, 5}; {7, 2}


Following the definitions above for our example, the **queen {4, 1}** occupies **row 4** , **column 1** , **left diagonal -3,** and **right diagonal 5**.

#### Write the Backtracking Algorithm

Now, it is time to write the recursive **backtracking algorithm** for placing the 8 queens.

The algorithm starts from row 0 and tries to place a queen at some column at row 0. On success, it tries to place the next queen at row 1, then the next queen at row 2, etc. until the last row is passed.

**Check If a Position is Free**

Now, let&#39;s write **the code to check whether a certain position is free**. A position is free when it is not under attack by any other queen. This means that if some of the rows, columns, or diagonals are already occupied by another queen, the position is occupied. Otherwise, it is free.

Recall that **col-row** is the number of the left diagonal and **row+col** is the number of the right diagonal.

#### Mark / Unmark Attacked Positions

After a queen is placed, we need to **mark as occupied all rows, columns, and diagonals** that it can attack.

On removal of a queen, we will need a method to mark as free all rows, columns, and diagonals that were attacked by it.

#### Print Solutions

When a solution is found, it should be printed on the console. First, introduce a solutions counter to simplify checking whether the found solutions are correct.

Next, pass through all rows and all columns at each row and **print the chessboard cells** :

#### Testing the Code

The &quot;8 queens&quot; puzzle has **92 distinct solutions**. Check whether your code generates and prints all of them correctly. The **solutions\_found** counter will help you check the number of solutions. Below are the 92 distinct solutions:


Submit your code in judge, printing all 92 solutions, separated by a single line.

#### Optimize the Solution

Now we can optimize our code:

- Remove the **attackedRows** set. It is not needed because all queens are placed consecutively at rows 0…7.
- Try to use **bool[]** array for **attackedColumns** , **attackedLeftDiagonals** and **attackedRightDiagonals** instead of sets. Note that arrays are indexed from 0 to their size and cannot hold negative indexes.


## 6. Recursive Fibonacci

Each member of the **Fibonacci sequence** is calculated from the **sum of the two previous members**. The first two elements are 1, 1. Therefore the sequence goes as 1, 1, 2, 3, 5, 8, 13, 21, 34…

The following sequence can be generated with an array, but that&#39;s easy, so **your task is to implement it recursively**.

If the function **GetFibonacci(n)** returns the nth Fibonacci number, we can express it using **GetFibonacci(n) = GetFibonacci(n-1) + GetFibonacci(n-2)**.

However, this will never end and in a few seconds a Stack Overflow Exception is thrown. In order for the recursion to stop it has to have a &quot;bottom&quot;. The bottom of the recursion is getFibonacci(1), and should return 1. The same goes for getFibonacci(0).

### Input

- On the only line in the input the user should enter the wanted Fibonacci number N where 1 ≤ N ≤ 49

### Output

- The output should be the nth Fibonacci number counting from 0

### Examples

| **Input** | **Output** |
| --- | --- |
| 5 | 8 |
| 10 | 89 |
| 21 | 17711 |

### Hint

For the nth Fibonacci number, we calculate the N-1st and the N-2nd number, but for the calculation of N-1st number we calculate the N-1-1st(N-2nd) and the N-1-2nd number, so we have a lot of repeated calculations.







