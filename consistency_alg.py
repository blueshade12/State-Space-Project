import pandas as pd
from collections import deque

class Arc_Consistency_Algorithm:
    def __init__(self, puzzle):
        self.puzzle = pd.DataFrame(puzzle)
        self.domains = self.initialize_domains()
        self.queue = self.initialize_queue()

    def run(self):
        if self.ac3():
            return self.backtrack()
        else:
            return None

    def backtrack(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle.iloc[row, col] == 0:
                    for value in range(1, 10):
                        if self.is_valid(row, col, value):
                            self.puzzle.iloc[row, col] = value
                            if self.backtrack():
                                return self.puzzle.values.tolist()
                            self.puzzle.iloc[row, col] = 0
                    return None
        return self.puzzle.values.tolist()

    def is_valid(self, row, col, value):
        for i in range(9):
            if self.puzzle.iloc[row, i] == value or self.puzzle.iloc[i, col] == value:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.puzzle.iloc[r, c] == value:
                    return False
        return True

    def initialize_domains(self):
        domains = {}
        for row in range(9):
            for col in range(9):
                if self.puzzle.iloc[row, col] == 0:
                    domains[(row, col)] = set(range(1, 10))
                else:
                    domains[(row, col)] = {self.puzzle.iloc[row, col]}
        return domains

    def initialize_queue(self):
        queue = deque()
        for row in range(9):
            for col in range(9):
                if self.puzzle.iloc[row, col] == 0:
                    neighbors = self.get_neighbors(row, col)
                    for neighbor in neighbors:
                        queue.append(((row, col), neighbor))
        return queue

    def get_neighbors(self, row, col):
        neighbors = set()
        for i in range(9):
            if i != col:
                neighbors.add((row, i))
            if i != row:
                neighbors.add((i, col))
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if r != row or c != col:
                    neighbors.add((r, c))
        return neighbors

    def ac3(self):
        while self.queue:
            (Xi, Xj) = self.queue.popleft()
            if self.revise(Xi, Xj):
                if len(self.domains[Xi]) == 0:
                    return False
                for Xk in self.get_neighbors(*Xi):
                    if Xk != Xj:
                        self.queue.append((Xk, Xi))
        return True

    def revise(self, Xi, Xj):
        revised = False
        for x in set(self.domains[Xi]):
            if not any(self.satisfies_constraint(x, y) for y in self.domains[Xj]):
                self.domains[Xi].remove(x)
                revised = True
        return revised

    def satisfies_constraint(self, x, y):
        return x != y
