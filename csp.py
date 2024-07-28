from typing import Generic

from csp_types import VariableT, AssignmentT
from constraint import Constraint


class CSP(Generic[VariableT]):
    def __init__(self, variables: list[VariableT], domains: dict[VariableT, set]):
        self.variables = variables
        self.domains = domains
        self.constraints: dict[VariableT, list[Constraint[VariableT]]] = {v: [] for v in self.variables}

    def add_constraint(self, constraint: Constraint[VariableT]):
        for variable in constraint.scope:
            assert variable in self.variables

            self.constraints[variable].append(constraint)

    def consistent(self, variable: VariableT, assignment: AssignmentT) -> bool:
        assert variable in self.variables, f"Expected to find variable {variable}!"

        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False

        return True

    def complete(self, assignment: AssignmentT) -> bool:
        for variable in self.variables:
            if variable not in assignment.keys():
                return False

        return True
