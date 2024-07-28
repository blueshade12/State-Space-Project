from csp_types import VariableT, AssignmentT
from csp import CSP
import pandas as pd


class BackTrackingAlgorithm:
    def __init__(self, puzzle):
        self.puzzle = pd.DataFrame(puzzle)

    def run(self):
        return self.backtracking_search(self.puzzle)

    def backtracking_search(self, csp):
        empty_assignment = dict()
        return self.backtrack(csp, empty_assignment)

    def backtrack(self, csp, assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        
        unassigned_variable = [v for v in csp.variables if v not in assignment]
        if not unassigned_variable:
            return None
        
        variable = unassigned_variable[0]
        
        for value in csp.domains(variable):
            assignment[variable] = value
            if csp.consistent(variable, assignment):
                result = self.backtrack(csp, assignment)
                if result is not None:
                    return result
                
            del assignment[variable]
        
        return None
                
            del assignment[variable]
        
        return None
