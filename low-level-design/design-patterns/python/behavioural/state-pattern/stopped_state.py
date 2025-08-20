from state import VMState


class StoppedError(Exception):
    pass


class StoppedState(VMState):
    def start(self, vm):
        from state_factory import StateFactory
        print(f"Starting VM {vm.name}")
        vm.set_state(StateFactory.get_starting_state())
    
    def stop(self, vm):
        print(f"VM {vm.name} is already in stopped state, no action performed")
        return StoppedError("VM is already in stopped state, no action performed")
    
    def restart(self, vm):
        from state_factory import StateFactory
        print(f"Restarting VM {vm.name}")
        vm.set_state(StateFactory.get_restarting_state())
    
    def suspend(self, vm):
        print(f"Cannot suspend VM {vm.name} as it is in stopped state")
        return StoppedError("Cannot suspend VM as it is in stopped state")
    
    def get_name(self):
        return "Stopped"