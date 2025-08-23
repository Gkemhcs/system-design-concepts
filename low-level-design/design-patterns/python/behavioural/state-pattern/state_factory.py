"""
State Factory to avoid circular imports
This factory provides access to state instances without importing them directly
"""

class StateFactory:
    """Factory class to create state instances and avoid circular imports"""
    
    _instances = {}
    
    @classmethod
    def get_starting_state(cls):
        """Get or create a StartingState instance"""
        if 'starting' not in cls._instances:
            from starting_state import StartingState
            cls._instances['starting'] = StartingState()
        return cls._instances['starting']
    
    @classmethod
    def get_stopped_state(cls):
        """Get or create a StoppedState instance"""
        if 'stopped' not in cls._instances:
            from stopped_state import StoppedState
            cls._instances['stopped'] = StoppedState()
        return cls._instances['stopped']
    
    @classmethod
    def get_restarting_state(cls):
        """Get or create a RestartingState instance"""
        if 'restarting' not in cls._instances:
            from restarting_state import RestartingState
            cls._instances['restarting'] = RestartingState()
        return cls._instances['restarting']
    
    @classmethod
    def get_suspended_state(cls):
        """Get or create a SuspendedState instance"""
        if 'suspended' not in cls._instances:
            from suspended_state import SuspendedState
            cls._instances['suspended'] = SuspendedState()
        return cls._instances['suspended']




