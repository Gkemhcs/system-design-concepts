from  vending_machine_state import VendingMachineState
from errors import InvalidBalance,VendingMachineOutofStock
from  vending_machine import    VendingMachine
class OutOfStockState(VendingMachineState):
    

    def insert_coin(self):
        raise VendingMachineOutofStock("the products are out of stock, try to check after sometime")
    def change_to_idle(self,machine:VendingMachine):
        from idle_state import IdleState
        if machine._inventory.get_available_product_stock():
            self.machine.change_state(IdleState())
        else:
            raise VendingMachineOutofStock("the products are out of stock, cannot be switched to idle state")
    def select_product(self,machine:VendingMachine):
        raise VendingMachineOutofStock("the products are out of stock, cannot select any product")
    def out_of_stock(self,machine:VendingMachine):
        raise VendingMachineOutofStock("already the machine is in out of stock state")
    def dispense_cash(self,machine:VendingMachine):
        raise VendingMachineOutofStock("the products are out of stock, cannot dispense any cash")