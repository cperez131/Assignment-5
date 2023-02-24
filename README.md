---
title: 'Assignment 5: Sudoku'
author: Assignment evolved at Pomona College through several instructors' offerings, with changes by Nathan Shelly and Sara Sood, Northwestern University. 
date: 'Due Day of Final (January 27-29)'
geometry: margin=1in
---

In this assignment, you will build your own Sudoku puzzle solver. We've provided starter code in a file named `a5.py`.

As discussed in class, we'll represent a state in the sudoku puzzle as a list of 9 lists each with 9 lists inside them. These innermost cells contain the assigned number if one has been assigned to it. Otherwise, the cell will contain a list of the remaining possible assignments. An `operation` in our approach will be to make an assignment to the "most constrained cell," that is, the cell with the least possible remaining assignments. The `update` function will involve removing possibilities from the lists after an assignment has been made. The `goal_test` will involve checking whether all cells in the board have been assigned. We'll also include a `failure_test` method that will check to see if there are cells that have no more possibilities.

The following sections will guide you through completing these functions and building a sudoku puzzle solver.

## Board

As discussed in class you will represent the sudoku board in a class called `Board`.

This class has the following attributes:

- `num_nums_placed`: the number of numbers placed on the board so far (initially 0)
- `size`: the size of the board (this will always be 9, but is convenient to have an attribute for this for debugging purposes)
- `rows`: this will be a list of 9 lists, each with 9 elements (imagine a 9x9 sudoku board). Each element will itself be a list of the numbers that remain possible to assign in that square. Initially, each element will contain a list of the numbers 1 through 9 as all numbers are possible when no assignments have been made. *Note:* this triply nested list will be confusing, don't feel dumb if it doesn't immediately make sense, I also get confused by it sometimes :). If you want to say set the value at a position in the board (make a square 7 for example) from a method you'd write something like this: `self.rows[row_index][col_index] = 7`. Here we're indexing into the first nested list to get the correct row, then indexing into that row to get the cell at the right column.

It should also contain the following methods (a few have already been provided, those are marked below):

- `__init__(self)` (*provided*): This should set `num_nums_placed` to 0, `size` to 9 and initialize `rows` to contain the initial representation of the board (before any numbers have been assigned). Each cell should include a list of the numbers from 1 to 9. **Note:** it is incredibly important to not change the names given here (the same names are in the docstring as well) as the autograder will fail if they are named anything else and you will lose points.
- `__str__(self)` (*provided*): returns a string representation of the board (yes, this will be hard to read).
- `print_pretty(self)` (*provided*): This method prints out a representation of the board with only the numbers that have been assigned. For cells that have yet to be assigned, they are printed out as `*` (as opposed to printing the list of possibilities).
- `subgrid_coordinates(self, row, col)` (*provided*): returns a list of `(row, column)` indices for all cells in the same region (the inner 3x3 grids) as the given `(row, col)` indices
- `find_most_constrained_cell(self)`: This method should return a tuple of the row and col position `(row, col)` that is "most constrained". The most constrained cell should be the cell that is the list with the least number of elements (possible assignments). Note: in the case of ties return the coordinates of the first minimum size cell found.
- `goal_test(self)`: returns `True` if the board is a complete solution, `False` otherwise. For the purposes of this solver this can be a simple function that just checks that we've placed the expected number of numbers (81 - the amount for a complete sudoku board). Note here that we're trusting our placement and update to catch invalid moves, not this method.
- `failure_test(self)`: returns `True` if the board has no possibility of leading to a correct solution. A good indication of whether or not it is a fail state involves seeing if any of the cells on the board contain an empty list.
- `update(self, row, column, assignment)`: Here `assignment` is a number to assign to the cell given by `row` & `column` arguments. It should then remove that assignment as a possibility from the candidate lists in the same row, column and `3*3` subgrid as the `(row, column)` index given. It should then set the given cell to the `assignment` number and update `num_nums_placed`. *Note:* we've provided a helper function called `remove_if_exists` that might be useful here. It takes a list and element to remove then removes that element from the list if it exists in the list.

Finally, outside of the board class, write a `DFS` function and a `BFS` function. These functions should utilize the `Stack` and `Queue` classes provided and follow the algorithm outlined in class. They will each take a board as input. This initial board should be added to the stack/queue. While the stack/queue is not empty, pop a board from the stack/queue to examine. If the board is a solution (`goal_test` returns `True`), return it. If a board is not a deadend (`failure_test` returns `False`) first find the most constrained cell on the board. Then try all possible assignments on that cell (adding all possible next states to the stack or queue).
*Hint:* this will involve a `for` loop over all assignments. For each assignment you'll want to create a *deepcopy* of the board before making the assignment.

After completing all of this work, notice the 2 boards initialized at the end of the starter code. When you run the code provided, the solution to each of the two provided puzzles should be printed. You should examine the printed boards to make sure they appear to be proper solutions.

Lastly, we've also provided two functions `is_valid` and `play_sudoku` at the bottom of the file to allow you to play. We can't let the computers have all the fun so uncomment the last couple of lines of the file to play yourself! (*Note:* you'll need to have completed the `Board` class **and** either also complete `BFS` & `DFS` or comment out the code that attempts to use them)

When you're done, upload your `a5.py` to github before the deadline.  Remember to continue to push to github throughout the process.  If you only have one push at the end of this assignment, then you will be docked points.
