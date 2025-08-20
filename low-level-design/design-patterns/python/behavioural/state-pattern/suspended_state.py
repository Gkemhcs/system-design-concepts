from abc import ABC,abstractmethod





class SuspendedError(Exception):
    pass 

from state import VMState


class SuspendedState(VMState):
    def start(self, vm):
        from state_factory import StateFactory
        print(f"Starting VM {vm.name}")
        vm.set_state(StateFactory.get_starting_state())
    
    def stop(self, vm):
        print(f"Cannot stop {vm.name} as it is already suspended")
        return SuspendedError("Cannot stop VM as it is already suspended")
    
    def restart(self, vm):
        from state_factory import StateFactory
        print(f"Restarting VM {vm.name}")
        vm.set_state(StateFactory.get_restarting_state())
    
    def suspend(self, vm):
        print(f"VM {vm.name} is already in suspended state, no action performed")
        return SuspendedError("VM is already in suspended state, no action performed")
    
    def get_name(self):
        return "Suspended"