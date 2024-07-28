from csp_types import AssignmentT
from constraint import Constraint


class RowConstraint(Constraint):
    def __init__(self, row):
        self.scope = [(row, col) for col in range(9)]
    
    def satisfied(self, assignment: AssignmentT) -> bool:
        values = set()
        for (row, col), value in assignment.items():
            if row == self.scope[0][0]:
                if value in values:
                    return False
                values.add(value)
        return True


class ColumnConstraint(Constraint):
    def __init__(self, col):
        self.scope = [(row, col) for row in range(9)]

    def satisfied(self, assignment: AssignmentT) -> bool:
        values = set()
        for (row, col), value in assignment.items():
            if col == self.scope[0][1]:
                if value in values:
                    return False
                values.add(value)
        return True


class GridNumberConstraint(Constraint):
    def __init__(self, start_row, start_col):
        self.scope = [(row, col) for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3)]

    def satisfied(self, assignment: AssignmentT) -> bool:
        values = set()
        for(row, col), value in assignment.items():
            if (row // 3, col // 3) == (self.scope[0][0] // 3, self.scope[0][1] // 3):
                if value in values:
                    return False
                values.add(value)
        return True


class CheckCellValue(Constraint):
    def __init__(self, cell: tuple[int, int]):
        self.scope = cell

    def satisfied(self, assignment: AssignmentT) -> bool:
        if assignment.get(self.scope[0]) is not None:
            value = assignment[self.scope[0]]
            return 1 <= value <= 9
        return True
