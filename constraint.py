from abc import ABC, abstractmethod
from typing import Generic

from csp_types import VariableT, AssignmentT


class Constraint(Generic[VariableT], ABC):
    def __init__(self, scope: list[VariableT]) -> None:
        self.scope = scope

    @abstractmethod
    def satisfied(self, assignment: AssignmentT) -> bool:
        pass
