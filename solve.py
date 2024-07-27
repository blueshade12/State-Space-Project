from typing import List, Tuple, Dict, Set

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
