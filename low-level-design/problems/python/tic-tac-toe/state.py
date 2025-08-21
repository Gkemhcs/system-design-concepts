from abc import ABC,abstractmethod 

class State(ABC):

    @abstractmethod
    def change_state(self,Board):
        pass

    