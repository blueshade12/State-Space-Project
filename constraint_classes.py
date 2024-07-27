from typing import Generic, TypeVar, List, Dict, Tuple, Optional
from abc import ABC, abstractmethod

VariableT = TypeVar("VariableT")
AssignmentT = Dict[VariableT, int]

class Constraint(Generic[VariableT], ABC):
    def __init__(self, scope: List[VariableT]) -> None:
        self.scope = scope

    @abstractmethod
    def satisfied(self, assignment: AssignmentT) -> bool:
        pass

class SudokuConstraint(Constraint[Tuple[int, int]]):
    def __init__(self) -> None:
        scope = [(row, col) for row in range(9) for col in range(9)]
        super().__init__(scope)

    def satisfied(self, assignment: AssignmentT) -> bool:
        def unique(values: List[int]) -> bool:
            values = [value for value in values if value != 0]
            return len(values) == len(set(values))

        for row in range(9):
            if not unique([assignment.get((row, col), 0) for col in range(9)]):
                return False
        for col in range(9):
            if not unique([assignment.get((row, col), 0) for row in range(9)]):
                return False

        for grid_row in range(3):
            for grid_col in range(3):
                if not unique([assignment.get((row, col), 0)
                               for row in range(grid_row * 3, (grid_row + 1) * 3)
                               for col in range(grid_col * 3, (grid_col + 1) * 3)]):
                    return False
        return True

class CSP(Generic[VariableT]):
    def __init__(self, variables: List[VariableT], domains: Dict[VariableT, List[int]]) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints: Dict[VariableT, List[Constraint[VariableT]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []

    def add_constraint(self, constraint: Constraint[VariableT]) -> None:
        for variable in constraint.scope:
            if variable in self.variables:
                self.constraints[variable].append(constraint)
            else:
                raise ValueError("Variable in constraint not in CSP")

    def consistent(self, variable: VariableT, assignment: AssignmentT) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def complete(self, assignment: AssignmentT) -> bool:
        return len(assignment) == len(self.variables)
