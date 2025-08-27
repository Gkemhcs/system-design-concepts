from abc import ABC,abstractmethod
from elevator import Elevator

class NextStopStrategy(ABC):

    @abstractmethod
    def get_next_stop(self, elevator: Elevator) -> int:
        pass 