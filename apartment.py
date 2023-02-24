import copy
from typing import List, Any, Tuple

# import Stack and Queue classes for BFS/DFS
from stack_and_queue import Stack, Queue

class Apt:

    def __init__(self):
        self.floors = [["C", "M", "S"] , ["B", "C", "F", "M", "S"], ["B", "C", "F", "M", "S"], ["B", "C", "F", "M", "S"], ["B", "S"]]
        self.nums_placed = 0

    def __str__(self):
        s = ""
        num = 5
        for row in self.floors:
            s += str(num) + ": "
            if isinstance(row, list):
                s += "-".join(row)
            else:
                s += row 
            s += "\n"
            num -= 1
        return s

    def failure_test(self):
        if self.floors[0] == "B" or self.floors[4] == "C" or self.floors[0] == "F" or self.floors[4] == "F":
            return True
        if "M" in self.floors and "C" in self.floors:
            print(self.floors.index("M") , ":" , self.floors.index("C")) 
            if self.floors.index("M") > self.floors.index("C"):
                return True
        if "S" in self.floors and "F" in self.floors:
            print("3rd")
            dif = self.floors.index("S") - self.floors.index("F") 
            if dif == 1 or dif == -1:
                return True
        if "C" in self.floors and "F" in self.floors:
            print("4th")
            dif = self.floors.index("C") - self.floors.index("F") 
            if dif == 1 or dif == -1:
                return True
        return False

    def find_most_constrained(self):
        cell = 0
        mini = 5
        for i in range(len(self.floors)):
            if isinstance(self.floors[i], list) and len(self.floors[i]) < mini:
                cell = i
                mini = len(self.floors[i])
        return cell

    def goal_test(self):
        return self.nums_placed == 5

    def update(self, floor, assignment):
        self.floors[floor] = assignment
        self.nums_placed += 1

        for i in range(len(self.floors)):
            if isinstance(self.floors[i], list) and assignment in self.floors[i]:
                self.floors[i].remove(assignment)

apt = Apt()
print(apt)
stack = Stack([apt])
while not stack.is_empty():
    curr: Apt = stack.pop()
    print(curr)
    if curr.goal_test():
        print("**********SOLUTION************")
        print(curr)
        break
    elif not curr.failure_test():
        c = curr.find_most_constrained()
        for el in curr.floors[c]:
            cpy = copy.deepcopy(curr)
            cpy.update(c, el)
            stack.push(cpy)
    
