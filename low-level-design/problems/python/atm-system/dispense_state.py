from machine_states import MachineState
from atm_system import ATMSystem
class DispenseState(MachineState):
    def insert_card(self,system:ATMSystem):
        raise NotImplementedError("sorry the system is already in dispense state")
    def authenticate_user(self,system:ATMSystem):
     
        raise NotImplementedError("sorry the card  has already  been authenticated")
        
    def display_transaction_types(self,system:ATMSystem):
        
        raise NotImplementedError("sorry the user has already selected transaction type")
      
    def dispense_cash(self,system:ATMSystem):
        
        raise NotImplementedError("sorry the system is already in dispense state")
        
    def change_to_idle(self,system:ATMSystem):
        from idle_state import IdleState
        if isinstance(system.get_current_state(),IdleState):
            raise Exception("sorry the system is already in idle state")
        system.remove_card()
        system.change_state(IdleState())