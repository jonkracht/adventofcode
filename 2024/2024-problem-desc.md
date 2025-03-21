# Problem Descriptions

## Day 15

1.  Given a list of actions and an environment (walls and moveable objects), determine the end state.
2.  Double the scale of the warehouse and repeat.


## Day 16

1.  Find an optimal maze solution where rotation (as opposed to continuing in the same direction) is heavily penalized.
2.  Find the number of maze locations that at least one optimal path pass through.

Solution:  Use Dijkstra to create graph, keeping track of both location and orientation.  Traverse graph to identify maze location on best paths.


## Day 17

1.  Code a simple program that processes and input integer and creates output from it.
2.  Find the smallest integer that when input into the program generates

Solution:  First part is fairly trivial.  Part Two was first solved by brute first search.  Further analysis of the program allowed all solutions to be found.


## Day 18

1.  Find the number of steps required to exit a maze.
2.  From a list of additional maze obstacles, find first that prevents exit from being possible.

Solution:  Use Dijkstra's algorithm to solve mazes.


## Day 19

1.  Find whether a target string can be created from a number of smaller of strings.  
2. Count the number of unique ways strings can be constructed.

Solution:  Use dynamic programming or memoization to cache intermediate string solutions so that they are simply looked-up rather than recomputed each time encountered.


## Day 20
