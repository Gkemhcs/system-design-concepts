from state import VMState




class StartingError(Exception):
    pass 


class StartingState(VMState):
    def start(self, vm):
        print(f"VM {vm.name} is already in started state, no action performed")
        return StartingError("VM is already in started state, no action performed")
    
    def stop(self, vm):
        from state_factory import StateFactory
        print(f"Stopping VM {vm.name}")
        vm.set_state(StateFactory.get_stopped_state())
    
    def restart(self, vm):
        from state_factory import StateFactory
        print(f"Restarting VM {vm.name}")
        vm.set_state(StateFactory.get_restarting_state())
    
    def suspend(self, vm):
        from state_factory import StateFactory
        print(f"Suspending VM {vm.name}")
        vm.set_state(StateFactory.get_suspended_state())
    
    def get_name(self):
        return "Starting"
