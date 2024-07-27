from abc import ABC, abstractmethod
from sudoku_reader import Sudoku_reader
from consistency_alg import Arc_Consistency_Algorithm
from backtracking_alg import Backtracking_Algorithm

class Constraint(ABC):
    @abstractmethod
    def run_algorithm(self):
        pass

class SudokuConstraint(Constraint):
    def __init__(self, algorithm_cls):
        self.path = input("Please input the filepath of the sudoku file: ")
        self.reader = Sudoku_reader()
        self.algorithm_cls = algorithm_cls

    def run_algorithm(self):
        puzzle = self.reader.sudoku_reader(self.path)
        alg = self.algorithm_cls(puzzle)  # Instantiate the selected algorithm
        return alg.run()

# To use Arc Consistency Algorithm
sudoku_constraint = SudokuConstraint(Arc_Consistency_Algorithm)
print(sudoku_constraint.run_algorithm())

# To use Backtracking Algorithm, uncomment the following lines:
# sudoku_constraint = SudokuConstraint(Backtracking_Algorithm)
# print(sudoku_constraint.run_algorithm())
