from vm import VM
from state_factory import StateFactory


def main():
    # Get initial state from factory
    starting_state = StateFactory.get_starting_state()
    
    # Create VM with initial state
    backend_vm = VM("backend-vm", starting_state)
    
    print(f"Initial VM state: {backend_vm.get_current_state()}")
    print("-" * 50)
    
    # Test state transitions
    print("Testing state transitions:")
    backend_vm.start()  # Should show already started message
    print(f"Current state: {backend_vm.get_current_state()}")
    print()
    
    backend_vm.stop()   # Should transition to stopped state
    print(f"Current state: {backend_vm.get_current_state()}")
    print()
    
    backend_vm.start()  # Should transition to starting state
    print(f"Current state: {backend_vm.get_current_state()}")
    print()
    
    backend_vm.suspend()  # Should transition to suspended state
    print(f"Current state: {backend_vm.get_current_state()}")
    print()
    
    backend_vm.restart()  # Should transition to restarting state
    print(f"Current state: {backend_vm.get_current_state()}")
    print()
    
    backend_vm.start()  # Should transition to starting state
    print(f"Current state: {backend_vm.get_current_state()}")


if __name__ == "__main__":
    main()
    