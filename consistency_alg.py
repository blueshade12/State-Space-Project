from sudoku_reader import Sudoku_reader
import pandas as pd
from collections import deque

class Arc_Consistency_Algorithm:
    def __init__(self, file_path):
        self.file_path = file_path
        self.instance_of_reader = Sudoku_reader()
        self.Xi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.puzzle = self.load_puzzle()
        self.domains = self.initialize_domains()
        self.queue = self.initialize_queue()

    def load_puzzle(self):
        return pd.DataFrame(self.instance_of_reader.sudoku_reader(self.file_path))

    def initialize_domains(self):
        domains = {}
        for index, row in self.puzzle.iterrows():
            for col, value in enumerate(row):
                if value == 0:
                    domains[(index, col)] = set(self.Xi)
                else:
                    domains[(index, col)] = {value}
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

    def get_constraints(self):
        constraint_dict = {}
        for index, row in self.puzzle.iterrows():
            for col, value in enumerate(row):
                if not isinstance(value, int) or value == 0:
                    constraint_list = []
                    for i in range(9):
                        constraint_list.append(self.puzzle.iloc[index, i])
                    constraint_dict[(index, col)] = constraint_list
        return constraint_dict

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
