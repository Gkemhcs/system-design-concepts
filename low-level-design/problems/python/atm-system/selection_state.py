from machine_states import MachineState 
from atm_system import ATMSystem

class SelectionState(MachineState):
    def insert_card(self,system:ATMSystem):
        raise NotImplementedError("sorry the system is already in selection state")
    def authenticate_user(self,system:ATMSystem):
     
        raise NotImplementedError("sorry the card  has already  been authenticated")
        
    def display_transaction_types(self,system:ATMSystem):
        
        raise NotImplementedError("sorry the user has already selected transaction type")
      
    def dispense_cash(self,system:ATMSystem):
        from dispense_state import DispenseState
        if not isinstance(system.get_current_state(),SelectionState):
           raise NotImplementedError("sorry the user hasn't selected transaction type cannot switch to dispense state at this time")
        system.change_state(DispenseState())
    def change_to_idle(self,system:ATMSystem):
        from idle_state import IdleState
        if not isinstance( system.get_current_state(),IdleState):
            raise Exception("sorry the system is already in idle state")
        system.change_state(IdleState())

    