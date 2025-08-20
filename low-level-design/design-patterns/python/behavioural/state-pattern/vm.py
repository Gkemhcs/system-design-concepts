from state import VMState


class VM:
    """Virtual Machine class that uses the State pattern"""
    
    def __init__(self, vm_name: str, initial_state: VMState):
        self.current_state = initial_state 
        self.name = vm_name
    
    def start(self) -> None:
        """Start the VM"""
        self.current_state.start(self)
    
    def stop(self) -> None:
        """Stop the VM"""
        self.current_state.stop(self)
    
    def restart(self) -> None:
        """Restart the VM"""
        self.current_state.restart(self)
    
    def suspend(self) -> None:
        """Suspend the VM"""
        self.current_state.suspend(self)
    
    def set_state(self, state: VMState) -> None:
        """Change the current state of the VM"""
        self.current_state = state
        print(f"VM {self.name} state changed to: {state.__class__.__name__}")
    
    def get_current_state(self) -> str:
        """Get the name of the current state"""
        return self.current_state.__class__.__name__
