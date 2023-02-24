import copy  # to make a deepcopy of the board
from typing import List, Any, Tuple

# import Stack and Queue classes for BFS/DFS
from stack_and_queue import Stack, Queue

# HELPER FUNCTION TO REMOVE ITEMS FROM A LIST
def remove_if_exists(lst: Any, elem: Any) -> None:
    """Takes a list and element and removes that element if it exists in the list

    Args:
        lst - the list you're trying to remove an item from
        elem - item to remove
    """
    if isinstance(lst, list) and elem in lst:
        lst.remove(elem)


# NOTE: The linter will complain at you due to the code using member variables like row,
# num_nums_placed & size since you haven't added those in the constructor. Implement the
# constructor before worrying about these errors (if they're still there after you've
# implemented the constructor that's probably a sign your constructor has a bug in it)
class Board:
    """Represents a state (situation) in a Sudoku puzzle. Some cells may have filled in
    numbers while others have not. Cells that have not been filled in hold the potential
    values that could be assigned to the cell (i.e. have not been ruled out from the
    row, column or subgrid)

    Attributes:
        num_nums_placed - number of numbers placed so far (initially 0)
        size - the size of the board (this will always be 9, but is convenient to have
            an attribute for this for debugging purposes)
        rows - a list of 9 lists, each with 9 elements (imagine a 9x9 sudoku board).
            Each element will itself be a list of the numbers that remain possible to
            assign in that square. Initially, each element will contain a list of the
            numbers 1 through 9 (so a triply nested 9x9x9 list to start) as all numbers
            are possible when no assignments have been made. When an assignment is made
            this innermost element won't be a list of possibilities anymore but the
            single number that is the assignment.
    """

    def __init__(self):
        """Constructor for a board, sets up a board with each element having all
        numbers as possibilities"""
        self.size: int = 9
        self.num_nums_placed: int = 0

        # triply nested lists, representing a 9x9 sudoku board
        # 9 quadrants, 9 cells in each 3*3 subgrid, 9 possible numbers in each cell
        # Note: using Any in the type hint since the cell can be either a list (when it
        # has not yet been assigned a value) or a value (once it has been assigned)
        # Note II: a lone underscore is a common convention for unused variables
        self.rows: List[List[Any]] = (
            [[list(range(1, 10)) for _ in range(self.size)] for _ in range(self.size)]
        )

    def __str__(self) -> str:
        """String representation of the board"""
        row_str = ""
        for r in self.rows:
            row_str += f"{r}\n"

        return f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}"

    def print_pretty(self):
        """Prints all numbers assigned to cells, excluding lists of possible numbers
        that can still be assigned to cells"""
        row_str = ""
        for i, r in enumerate(self.rows):
            if not i % 3:
                row_str += " -------------------------\n"

            for j, x in enumerate(r):
                row_str += " | " if not j % 3 else " "
                row_str += "*" if isinstance(x, list) else f"{x}"

            row_str += " |\n"

        row_str += " -------------------------\n"
        print(f"num_nums_placed: {self.num_nums_placed}\nboard (rows): \n{row_str}")

    def subgrid_coordinates(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Get all coordinates of cells in a given cell's subgrid (3x3 space)

        Integer divide to get column & row indices of subgrid then take all combinations
        of cell indices with the row/column indices from those subgrids (also known as
        the outer or Cartesian product)

        Args:
            row - index of the cell's row, 0 - 8
            col - index of the cell's col, 0 - 8

        Returns:
            list of (row, col) that represent all cells in the box.
        """
        subgrids = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
        # Note: row // 3 gives the index of the subgrid for the row index, this is one
        # of 0, 1 or 2, col // 3 gives us the same for the column
        return [(r, c) for c in subgrids[col // 3] for r in subgrids[row // 3]]

    def find_most_constrained_cell(self) -> Tuple[int, int]:
        """Finds the coordinates (row and column indices) of the cell that contains the
        fewest possible values to assign (the shortest list). Note: in the case of ties
        return the coordinates of the first minimum size cell found

        Returns:
            a tuple of row, column index identifying the most constrained cell
        """
        pass

    def failure_test(self) -> bool:
        """Check if we've failed to correctly fill out the puzzle. If we find a cell
        that contains an [], then we have no more possibilities for the cell but haven't
        assigned it a value so fail.

        Returns:
            True if we have failed to fill out the puzzle, False otherwise
        """
        pass

    def goal_test(self) -> bool:
        """Check if we've completed the puzzle (if we've placed all the numbers).
        Naively checks that we've placed as many numbers as cells on the board

        Returns:
            True if we've placed all numbers, False otherwise
        """
        pass

    def update(self, row: int, column: int, assignment: int) -> None:
        """Assigns the given value to the cell given by passed in row and column
        coordinates. By assigning we mean set the cell to the value so instead the cell
        being a list of possibities it's just the new assignment value.  Update all
        affected cells (row, column & subgrid) to remove the possibility of assigning
        the given value.

        Args:
            row - index of the row to assign
            column - index of the column to assign
            assignment - value to place at given row, column coordinate
        """
        pass


def DFS(state: Board) -> Board:
    """Performs a depth first search. Takes a Board and attempts to assign values to
    most constrained cells until a solution is reached or a mistake has been made at
    which point it backtracks.

    Args:
        state - an instance of the Board class to solve, need to find most constrained
            cell and attempt an assignment

    Returns:
        either None in the case of invalid input or a solved board
    """
    pass


def BFS(state: Board) -> Board:
    """Performs a breadth first search. Takes a Board and attempts to assign values to
    most constrained cells until a solution is reached or a mistake has been made at
    which point it backtracks.

    Args:
        state - an instance of the Board class to solve, need to find most constrained
            cell and attempt an assignment

    Returns:
        either None in the case of invalid input or a solved board
    """
    pass


if __name__ == "__main__":
    # CODE BELOW HERE RUNS YOUR BFS/DFS
    print("<<<<<<<<<<<<<< Solving Sudoku >>>>>>>>>>>>>>")

    def test_dfs_or_bfs(use_dfs: bool, moves: List[Tuple[int, int, int]]) -> None:
        b = Board()
        # make initial moves to set up board
        for move in moves:
            b.update(*move)

        # print initial board
        print("<<<<< Initial Board >>>>>")
        b.print_pretty()
        # solve board
        solution = (DFS if use_dfs else BFS)(b)
        # print solved board
        print("<<<<< Solved Board >>>>>")
        solution.print_pretty()

    # sets of moves for the different games
    first_moves = [
        (0, 1, 7),
        (0, 7, 1),
        (1, 2, 9),
        (1, 3, 7),
        (1, 5, 4),
        (1, 6, 2),
        (2, 2, 8),
        (2, 3, 9),
        (2, 6, 3),
        (3, 1, 4),
        (3, 2, 3),
        (3, 4, 6),
        (4, 1, 9),
        (4, 3, 1),
        (4, 5, 8),
        (4, 7, 7),
        (5, 4, 2),
        (5, 6, 1),
        (5, 7, 5),
        (6, 2, 4),
        (6, 5, 5),
        (6, 6, 7),
        (7, 2, 7),
        (7, 3, 4),
        (7, 5, 1),
        (7, 6, 9),
        (8, 1, 3),
        (8, 7, 8),
    ]

    second_moves = [
        (0, 1, 2),
        (0, 3, 3),
        (0, 5, 5),
        (0, 7, 4),
        (1, 6, 9),
        (2, 1, 7),
        (2, 4, 4),
        (2, 7, 8),
        (3, 0, 1),
        (3, 2, 7),
        (3, 5, 9),
        (3, 8, 2),
        (4, 1, 9),
        (4, 4, 3),
        (4, 7, 6),
        (5, 0, 6),
        (5, 3, 7),
        (5, 6, 5),
        (5, 8, 8),
        (6, 1, 1),
        (6, 4, 9),
        (6, 7, 2),
        (7, 2, 6),
        (8, 1, 4),
        (8, 3, 8),
        (8, 5, 7),
        (8, 7, 5),
    ]

    print("<<<<<<<<<<<<<< Testing DFS on First Game >>>>>>>>>>>>>>")

    test_dfs_or_bfs(True, first_moves)

    print("<<<<<<<<<<<<<< Testing DFS on Second Game >>>>>>>>>>>>>>")

    test_dfs_or_bfs(True, second_moves)

    print("<<<<<<<<<<<<<< Testing BFS on First Game >>>>>>>>>>>>>>")

    test_dfs_or_bfs(False, first_moves)

    print("<<<<<<<<<<<<<< Testing BFS on Second Game >>>>>>>>>>>>>>")

    test_dfs_or_bfs(False, second_moves)
