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

    def setup_sudoku(puzzle: str) -> Tuple[List[Tuple[int, int]], Dict[Tuple[int, int], Set[int]], Dict[Tuple[int, int], int]]:
      variables = [(r, c) for r in range(9) for c in range(9)]
      domains = {var: set(range(1, 10)) for var in variables}
      initial_assignment = {}

      for r in range(9):
          for c in range(9):
              value = int(puzzle[r * 9 + c])
              if value != 0:
                  initial_assignment[(r, c)] = value
                  domains[(r, c)] = {value}

      return variables, domains, initial_assignment
