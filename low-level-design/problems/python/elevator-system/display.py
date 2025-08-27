from elevator_observer import ElevatorObserver
from elevator_state import ElevatorState
class Display(ElevatorObserver):

    def on_state_change(self,elevator_id:int,from_state:ElevatorState,to_state:ElevatorState):

        print(f"the elevator [{elevator_id}] has been changed from {from_state} to {to_state}")
    def on_floor_change(self,elevator_id:int,floor:int):
        print(f"the elevator [{elevator_id}] has reached floor {floor}")

