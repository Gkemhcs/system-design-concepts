from abc import ABC,abstractmethod

class VendingMachineState(ABC):

    @abstractmethod
    def insert_coin(self):
        

    @staticmethod
    def select_product(self):
        pass 

    @staticmethod
    def dispense_cash(self):
        pass 


    @staticmethod
    def out_of_stock(self):
        pass 
    
    @staticmethod
    def change_to_idle(self):
        pass