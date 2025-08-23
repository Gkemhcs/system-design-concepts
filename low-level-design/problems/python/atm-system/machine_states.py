from abc import ABC,abstractmethod

class MachineState(ABC):

    @abstractmethod
    def insert_card(self):
        pass 

    @abstractmethod
    def authenticate_user(self):
        pass 

    @abstractmethod
    def display_transaction_types(self):
        pass 


    @abstractmethod
    def dispense_cash(self):
        pass 

    @abstractmethod
    def change_to_idle(self):
        pass 
