from state import VMState





class RestartingError(Exception):
    pass 


class RestartingState(VMState):
    def start(self, vm):
        from state_factory import StateFactory
        print(f"Starting VM {vm.name}")
        vm.set_state(StateFactory.get_starting_state())
    
    def stop(self, vm):
        from state_factory import StateFactory
        print(f"Stopping VM {vm.name}")
        vm.set_state(StateFactory.get_stopped_state())
    
    def restart(self, vm):
        print(f"VM {vm.name} is already in restarting state, no action performed")
        return RestartingError("VM is already in restarting state, no action performed")
    
    def suspend(self, vm):
        from state_factory import StateFactory
        print(f"Suspending VM {vm.name}")
        vm.set_state(StateFactory.get_suspended_state())
    
    def get_name(self):
        return "Restarting"