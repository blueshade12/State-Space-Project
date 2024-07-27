from typing import Generic, TypeVar, List, Dict

VariableT = TypeVar("VariableT")
AssignmentT = Dict[VariableT, int]

class Backtracking_Algorithm(Generic[VariableT]):
    def __init__(self, csp: VariableT) -> None:
        self.csp = csp

    def run(self) -> AssignmentT:
       return self.backtracking_search()
       """
        if self.backtrack():
            return self.backtracking_search()
        else:
            return None
       
        """

    def backtracking_search(self) -> AssignmentT:
        empty_assignment = {}
        return self.backtrack(empty_assignment)

    def backtrack(self, assignment: AssignmentT) -> AssignmentT:
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

    def select_unassigned_variable(self, assignment: Dict[VariableT, int]) -> VariableT:
        unassigned = [v for v in self.csp.variables if v not in assignment]
        return min(unassigned, key=lambda var: len(self.csp.domains[var]))
