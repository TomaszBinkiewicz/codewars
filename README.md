# Content

* [Unary messages](#unary-messages)
* [Sudoku solver](#sudoku-solver)

## Unary messages

Binary with 0 and 1 is good, but binary with only 0 is even better! Originally, this is a concept designed by Chuck Norris to send so called unary messages.

Can you write a program that can send and receive this messages?

#### Rules
The input message consists of ASCII characters between 32 and 127 (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
First block is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
The number of 0 in the second block is the number of bits in the series
Example
Let’s take a simple example with a message which consists of only one character (Letter 'C').
'C' in binary is represented as 1000011, so with Chuck Norris’ technique this gives:
0 0 - the first series consists of only a single 1
00 0000 - the second series consists of four 0
0 00 - the third consists of two 1
So 'C' is coded as: 0 0 00 0000 0 00

Second example, we want to encode the message "CC" (i.e. the 14 bits 10000111000011) :
0 0 - one single 1
00 0000 - four 0
0 000 - three 1
00 0000 - four 0
0 00 - two 1
So "CC" is coded as: 0 0 00 0000 0 000 00 0000 0 00

## Sudoku solver

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.
The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
For Sudoku rules, see the [Wikipedia article](https://en.wikipedia.org/wiki/Sudoku).

```
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)

# Should return
 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
```