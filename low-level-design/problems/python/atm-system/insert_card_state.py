from machine_states import MachineState
from atm_system import ATMSystem

class InsertCardState(MachineState):

    def insert_card(self,system:ATMSystem):
        raise NotImplementedError("sorry the system is already in insert_card state")
    def authenticate_user(self,system:ATMSystem):
        from authenticated_state import AuthenticatedState
        if not isinstance(system.get_current_state(),InsertCardState):
            raise NotImplementedError("sorry the card hasn;t been inserted so cannot authenticate user")
        system.change_state(AuthenticatedState())
    def display_transaction_types(self,system:ATMSystem):
        raise NotImplementedError("sorry the user hasn't been authenticated yet cannot display transactions")
    def dispense_cash(self,system:ATMSystem):
        raise NotImplementedError("sorry the user hasn't been authenticated yet  cannot dispense cash at this time")
    def change_to_idle(self,system:ATMSystem):
        from idle_state import IdleState
        if not isinstance(system.get_current_state(),IdleState):
            raise Exception("sorry the system is already in idle state")
        system.change_state(IdleState())
