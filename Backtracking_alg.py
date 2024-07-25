class BacktrackingAlgorithm(Generic[VariableT]):
    def __init__(self, csp: CSP[VariableT]) -> None:
        self.csp = csp

    def backtracking_search(self) -> Dict[VariableT, int]:
        empty_assignment = {}
        return self.backtrack(empty_assignment)

    def backtrack(self, assignment: Dict[VariableT, int]) -> Dict[VariableT, int]:
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


    def solve_sudoku(self, puzzle):
      self.variables = [(i, j) for i in range(9) for j in range(9)]
      domains = {var: set(range(1, 10)) for var in self.variables}
      for i in range(9):
          for j in range(9):
            if puzzle[i][j] != 0:
                domains[(i, j)] = {puzzle[i][j]}
      csp = CSP(self.variables, domains)
      csp.add_constraint(SudokuConstraint(self.variables))
      solver = BacktrackingAlgorithm(csp)
      return solver.backtracking_search()
