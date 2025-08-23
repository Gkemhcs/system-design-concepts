from __future__ import annotations
from machine_states import MachineState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atm_system import ATMSystem

class IdleState(MachineState):

    def insert_card(self, system: ATMSystem):
        from insert_card_state import InsertCardState
        
        if not isinstance(system.get_current_state(),IdleState):
            raise NotImplementedError("the atm is not in idle state")
        system.change_state(InsertCardState())
    
    def authenticate_user(self, system: ATMSystem):
        raise NotImplementedError("sorry the card hasn't been inserted to idle state")
    
    def display_transaction_types(self, system: ATMSystem):
        raise NotImplementedError("sorry the card hasn't been inserted to display the transaction types")
    
    def dispense_cash(self, system: ATMSystem):
        raise NotImplementedError("sorry the card hasn't been inserted to dispense the cash")
    
    def change_to_idle(self, system: ATMSystem):
        raise NotImplementedError("sorry the atm is already in idle state")
    
