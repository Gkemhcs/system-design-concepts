from inventory import Inventory 
from cash_registrar import CashRegistrar
from vending_machine_state import 


class VendingMachine:

    def __init__(self,cash_registrar:CashRegistrar):
         
        self._inventory:Inventory=None
        self.cash_registrar=cash_registrar
        self.current_state=