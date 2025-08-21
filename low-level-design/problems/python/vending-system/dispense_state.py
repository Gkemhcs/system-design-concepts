from vending_machine_state import VendingMachineState
from vending_machine import VendingMachine
class  DispenseState(VendingMachineState):
    def insert_coin(self,machine:VendingMachine):
        raise NotImplementedError("Cannot insert coin in dispense state")
    def select_product(self,machine:VendingMachine):
        raise NotImplementedError("Cannot select product in dispense state")
    def dispense_cash(self,machine:VendingMachine):
        raise NotImplementedError("Cannot dispense cash in dispense state")
    def out_of_stock(self,machine:VendingMachine):
        raise NotImplementedError("Cannot mark out of stock in dispense state")
    def change_to_idle(self,machine:VendingMachine):
        from idle_state import IdleState
        machine.change_state(IdleState())
    
