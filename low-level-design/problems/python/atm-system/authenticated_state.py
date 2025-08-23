from __future__ import annotations
from machine_states import MachineState
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from atm_system import ATMSystem

class AuthenticatedState(MachineState):

    def insert_card(self, system: ATMSystem):
        raise NotImplementedError("sorry the system is already in authenticated state")
    
    def authenticate_user(self, system: ATMSystem):
        raise NotImplementedError("sorry the card has already been authenticated")
        
    def display_transaction_types(self, system: ATMSystem):
        from selection_state import SelectionState
        if not isinstance(system.get_current_state(), AuthenticatedState):
            raise NotImplementedError("sorry the user hasn't been authenticated yet")
        system.change_state(SelectionState())
    
    def dispense_cash(self, system: ATMSystem):
        from dispense_state import DispenseState
        # Change to dispense state for cash operations
        system.change_state(DispenseState())
    
    def change_to_idle(self, system: ATMSystem):
        from idle_state import IdleState
        if isinstance(system.get_current_state(), IdleState):
            raise Exception("sorry the system is already in idle state")
        system.change_state(IdleState())

    