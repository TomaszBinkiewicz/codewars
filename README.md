# Content
In this repository you can find some of my solutions to kata from
[<img width="50" src="https://raw.githubusercontent.com/Codewars/codewars.com/master/docs/assets/img/logo.png" alt="codewors">](https://www.codewars.com)

* [Unary messages](#unary-messages)
* [Sudoku solver](#sudoku-solver)
* [Is my friend cheating?](#is-my-friend-cheating)
* [Human readable duration format](#human-readable-duration-format)

## Unary messages

**Rank: 6 kyu**
[Link to kata](https://www.codewars.com/kata/5e5ccbda30e9d0001ec77bb6)

### Description
Binary with 0 and 1 is good, but binary with only 0 is even better! Originally, this is a concept designed by Chuck
Norris to send so called unary messages.

Can you write a program that can send and receive this messages?

### Rules
* The input message consists of ASCII characters between 32 and 127 (7-bit)
* The encoded output message consists of blocks of 0
* A block is separated from another block by a space
* Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
* First block is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
* The number of 0 in the second block is the number of bits in the series

##### Example
Let’s take a simple example with a message which consists of only one character (Letter 'C').
'C' in binary is represented as 1000011, so with Chuck Norris’ technique this gives:
0 0 - the first series consists of only a single 1
00 0000 - the second series consists of four 0
0 00 - the third consists of two 1
So 'C' is coded as: 0 0 00 0000 0 00


##### Another example
We want to encode the message "CC" (i.e. the 14 bits 10000111000011) :
0 0 - one single 1
00 0000 - four 0
0 000 - three 1
00 0000 - four 0
0 00 - two 1
So "CC" is coded as: 0 0 00 0000 0 000 00 0000 0 00

## Sudoku solver

**Rank: 3 kyu**
[Link to kata](https://www.codewars.com/kata/5296bc77afba8baa690002d7)

### Description

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle
array, with the value 0 representing an unknown square.
The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test
possibilities on unknowns) and can be solved with a brute-force approach.
For Sudoku rules, see the [Wikipedia article](https://en.wikipedia.org/wiki/Sudoku).

##### Example
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
```
Should return:

```
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

## Is my friend cheating?

**Rank: 5 kyu**
[Link to kata](https://www.codewars.com/kata/5547cc7dcad755e480000004)

### Rules

* A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
* Within that sequence, he chooses two numbers, a and b.
* He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
* Given a number n, could you tell me the numbers he excluded from the sequence?

The function takes the parameter: n (n is always strictly greater than 0) and returns an array of the form:
`[(a, b), ...]`
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

`[(a, b), ...]` will be sorted in increasing order of the "a".

It happens that there are several possible (a, b). The function returns an empty array if no possible numbers are found
which will prove that my friend has not told the truth!.


##### Examples
```
removNb(26) should return [(15, 21), (21, 15)]
```
```
removNb(100) should return []
```

## Human readable duration format

**Rank: 4 kyu**
[Link to kata](https://www.codewars.com/kata/52742f58faf5485cae000b9a)

### Description

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is 
expressed as a combination of years, days, hours, minutes and seconds.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

### Rules 

* The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
  the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
* The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", 
  just like it would be written in English.
* A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not
  correct, but 1 year and 1 second is.
* Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
* A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it
  should be just 1 minute.
* A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 
  minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid 
  more significant unit of time.

##### Examples

```
format_duration(62)    # returns "1 minute and 2 seconds"
```
```
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
```







## Snakes and ladders

**Rank: 4 kyu**
[Link to kata](https://www.codewars.com/kata/587136ba2eefcb92a9000027)

### Description

Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. It is played between two or 
more players on a gameboard having numbered, gridded squares. A number of "ladders" and "snakes" are pictured on the 
board, each connecting two specific board squares. (Source [Wikipedia](https://en.wikipedia.org/wiki/Snakes_and_Ladders)) 

Your task is to make a simple class called SnakesLadders. The test cases will call the method play(die1, die2) 
independantly of the state of the game or the player turn. The variables die1 and die2 are the die thrown in a turn and 
are both integers between 1 and 6. The player will move the sum of die1 and die2.

### The board

<img src="https://raw.githubusercontent.com/adrianeyre/codewars/master/Ruby/Authored/snakesandladdersboard.jpg" alt="loading error" width="500">

### Rules 

* There are two players and both start off the board on square 0.
* Player 1 starts and alternates with player 2.
* You follow the numbers up the board in order 1=>100
* If the value of both die are the same then that player will have another go.
* Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly 
  on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square
  at the top of the ladder. (even if you roll a double).
* Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the 
  top of a snake, slide move the player all the way to the square at the bottom of the snake or chute 
  (even if you roll a double).
* Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's 
  a twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling 
  the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your 
  game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

##### Returns

`Player n is on square x`. Where n is the current player and x is the sqaure they are currently on.

`Player n Wins!` where n is winning player that has landed on square 100 without any remainding moves left.

`Game over!` if a player has won and another player tries to play.

---
---
#### My current rank

<img src="https://www.codewars.com/users/b_t_y/badges/micro" alt="loading error">
