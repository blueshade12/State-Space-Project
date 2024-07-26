from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Dict, Set, Tuple

VariableT = TypeVar("VariableT")
AssignmentT = Dict[VariableT, int]


class Constraint(Generic[VariableT], ABC):
    def __init__(self, scope: List[VariableT]) -> None:
        self.scope = scope

    @abstractmethod
    def satisfied(self, assignment: AssignmentT) -> bool:
        pass
