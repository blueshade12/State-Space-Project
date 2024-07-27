from typing import Generic, TypeVar, List, Dict, Set
from abstract_class import Constraint

VariableT = TypeVar("VariableT")
AssignmentT = Dict[VariableT, int]


class CSP(Generic[VariableT]):
    def __init__(self, variables: List[VariableT], domains: Dict[VariableT, Set[int]]) -> None:
        self.variables = variables
        self.domains = domains
        self.constraints: Dict[VariableT, List[Constraint]] = {v: [] for v in self.variables}

    def add_constraint(self, constraint: Constraint):
        for variable in constraint.scope:
            if variable not in self.variables:
                raise ValueError
            self.constraints[variable].append(constraint)

    def consistent(self, variable: VariableT, assignment: AssignmentT) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def complete(self, assignment: AssignmentT) -> bool:
        return all(variable in assignment for variable in self.variables)
    
