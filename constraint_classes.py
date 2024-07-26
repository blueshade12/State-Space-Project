class Constraint(Generic[VariableT], ABC):
    def __init__(self, scope: List[VariableT]) -> None:
        self.scope = scope

    @abstractmethod
    def satisfied(self, assignment: AssignmentT) -> bool:
        pass


class SudokuConstraint(Constraint[Tuple[int, int]]):
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
