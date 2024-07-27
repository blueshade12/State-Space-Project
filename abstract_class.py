from abc import ABC, abstractmethod
from SudokuReader import Sudoku_reader


class Constraint(ABC):
    @abstractmethod
    def run_algorithm(self):
        pass

class SudokuConstraint(Constraint):
    def __init__(self):
        self.path = input("Please input the filepath of the sudoku file: ")
        self.reader = Sudoku_reader()
        self.solved_puzzle = self.run_algorithm()

    def run_algorithm(self):
        puzzle = self.reader.sudoku_reader(self.path)
        from Backtracking import Backtracking_Algorithm
        alg = Backtracking_Algorithm(puzzle)
        return alg.run()

sudoku_constraint = SudokuConstraint()
print(sudoku_constraint.solved_puzzle)
