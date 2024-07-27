from typing import List, Dict, Optional
from constraint_classes import CSP, SudokuConstraint

class Backtracking_Algorithm:
    def __init__(self, puzzle: List[List[int]]) -> None:
        self.puzzle = puzzle
        self.variables = [(row, col) for row in range(9) for col in range(9)]
        self.domains = {(row, col): list(range(1, 10)) if puzzle[row][col] == 0 else [puzzle[row][col]] for row in range(9) for col in range(9)}
        self.csp = CSP(self.variables, self.domains)
        self.csp.add_constraint(SudokuConstraint())

    def run(self) -> Optional[List[List[int]]]:
        assignment = {(row, col): self.puzzle[row][col] for row in range(9) for col in range(9) if self.puzzle[row][col] != 0}
        result = self.backtrack(assignment)
        if result is None:
            return None
        else:
            for row in range(9):
                for col in range(9):
                    self.puzzle[row][col] = result[(row, col)]
            return self.puzzle

    def backtrack(self, assignment: Dict[tuple[int, int], int]) -> Optional[Dict[tuple[int, int], int]]:
        if self.csp.complete(assignment):
            return assignment

        variable = self.select_unassigned_variable(assignment)
        for value in self.csp.domains[variable]:
            if self.csp.consistent(variable, {**assignment, variable: value}):
                assignment[variable] = value
                result = self.backtrack(assignment)
                if result is not None:
                    return result
                del assignment[variable]
        return None

    def select_unassigned_variable(self, assignment: Dict[tuple[int, int], int]) -> tuple[int, int]:
        unassigned = [v for v in self.csp.variables if v not in assignment]
        return min(unassigned, key=lambda var: len(self.csp.domains[var]))
