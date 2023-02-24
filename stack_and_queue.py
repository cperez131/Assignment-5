from typing import Generic, List, TypeVar

# the Stack and Queue classes for DFS and BFS

# stack element type variable
S = TypeVar("S")
# queue element type variable
Q = TypeVar("Q")


class Stack:
    """A last in first out (LIFO) stack representation where elements are pushed and
    popped from the top. Think of a stack of plates, where you can't remove or add a
    plate in the middle, only take from, or add to, the top

    Attributes:
        the_stack - the list that holds the elements of our stack
    """

    def __init__(self, initial: List[S] = []) -> None:
        """Constructor for a stack, set the stack up with the given list if any is
        provided otherwise empty

        Args:
            initial - optional list of elements to fill the stack with
        """

        # can't have lists (mutable objects in general) as default values as the default
        # is shared among all instances. need to copy here to avoid issues with aliases
        self.the_stack: List[S] = initial[:]

    def __str__(self) -> str:
        """String representation of the stack"""
        return f"The stack contains: {self.the_stack}"

    def is_empty(self) -> bool:
        """Check if stack has no elements

        Returns:
            True if stack has no elements, False otherwise
        """
        return len(self.the_stack) == 0

    def push(self, elt: S) -> None:
        """Add element (elt) to top of stack

        Args:
            elt - an item to add to the stack
        """
        self.the_stack.append(elt)

    def pop(self) -> S:
        """Remove and return the top item in the stack (corresponds to the last item in
        the list)

        Returns:
            the most recently added element
        """
        return self.the_stack.pop()


class Queue:
    """A first in first out (FIFO) queue representation where elements are pushed at the
    end of the queue and popped from the front. Think of a line at an amusement park
    where new people join (pushed) the line at the back and are let in (popped) from the
    front

    Attributes:
        the_queue - the list that holds the elements of our queue
    """

    def __init__(self, initial: List[Q] = []) -> None:
        """Constructor for a queue, simply sets the queue up with the given list if any
        is provided otherwise empty

        Args:
            initial - optional list of elements to fill the queue with
        """

        # can't have lists (mutable objects in general) as default values as the default
        # is shared among all instances. need to copy here to avoid issues with aliases
        self.the_queue: List[Q] = initial[:]

    def __str__(self) -> str:
        """String representation of the queue"""
        return f"The queue contains: {self.the_queue}"

    def is_empty(self) -> bool:
        """Check if queue has no elements

        Returns:
            True if queue has no elements, False otherwise
        """
        return len(self.the_queue) == 0

    def push(self, elt: Q) -> None:
        """Add element (elt) to end of queue

        Args:
            elt - an item to add to the queue
        """
        self.the_queue.append(elt)

    def pop(self) -> Q:
        """Remove and return the start of the queue (corresponds to the first item in
        the list)

        Returns:
            the oldest added element
        """
        return self.the_queue.pop(0)
