#### Sudoku Solver
### How to Run the program

First, paste the board configiration with an extra line at the ending into a file called input.txt, then run the following

		python <program>

It should output you the final solution with the number of backtracking steps involved in total as well as the run time of the program. I've commented the code so that it is easy to understand. I've also mentioned some test cases for which the code worked well.

### Naive Backtracking

The basic backtracking method by going through each empty slot on the board and checking for all the values 1-9, if a particular number can be placed or not( If the other constraints don't allow it, I need to backtrack to the previous position where another number is checked for validity). I am going row-by-row in search of empty slots on the board. This is a naive method as it results in a lot of unnecessary branching.

### Smart Backtracking

Here, I've used both the minimum remaining values and the forward checking heuristics along with the backtracking followed in the naive algorithm. After the naive backtracking method, in quest of improving the performance, we have 3 goals in mind.

* Which variable should we fill first?
* Which value should be assigned to a variable?  
* Is there any way which can tell us that we may get struck somewhere even before reaching that position

**Most constraining variable**: So, while playing sudoku what we do first?? Filling the empty spaces whose domain is less is the first thing we would do as humans. Why not incorporate the same logic to the machine which thinks like us. This way we can fill some of the spots easily within no time. I compute the remaining legal values of all the empty spots initially based on the initial board configuration. Then I choose the block with least legal moves.

**Least Constraining value**: Filling the spot with a value from the domain results in an update of domains for all the blocks which are related to the former box. Remove the currently filled number from the domains of all the boxes in the same row, column and sub-box. Then find the box with least legal moves again and continue.


**Forward Checking**: While doing this method, there would be a position where the domain of a box can go empty, which means the box has no remaining legal moves. That means the branch which we considered is wrong and we need to backtrack. This is found even before reaching the state where there is no move for a block. So we are looking ahead what can happen in the future if we go through any branch from this position by storing the remaining legal moves of all blocks and updating them every time.


This improved the performance a lot especially in case of evil test cases as we may reduce a lot of unnecessary branching this way.



### Analysis:

Both the algorithms are working fine for all the test cases (easy, medium, hard and evil) but the only difference I found was the number of backtracking steps that takes place in part2 is way lesser that part1.


For the following test case:

Sudoku 05  
008640500  
000000000  
052000000  
040906010  
020804060  
080307020  
000000370  
000000000  
001082400  


No.of backtracking steps in Part1: 104866		Runtime: 1.419292  
No.of backtracking steps in Part2: 91			Runtime: 0.005799


Similiiarly for,

Sudoku 04  
000170450  
000008173  
000000800  
340000500  
000609000  
009000036  
005000000  
874900000  
013027000  

No.of backtracking steps in Part1: 1913	Runtime: 0.023849s  
No.of backtracking steps in Part2: 111			Runtime: 0.006754s

We can see the number of backtracking's for the same input differ in millions which is a lot.

![Image](./figure1_jpeg)
