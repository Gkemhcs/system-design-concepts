from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Use TYPE_CHECKING to avoid circular imports at runtime
if TYPE_CHECKING:
    from vm import VM


class VMState(ABC):
    """Abstract base class for VM states"""
    
    @abstractmethod
    def start(self, vm: 'VM') -> None:
        """Start the VM"""
        pass 
    
    @abstractmethod
    def stop(self, vm: 'VM') -> None:
        """Stop the VM"""
        pass 
    
    @abstractmethod
    def restart(self, vm: 'VM') -> None:
        """Restart the VM"""
        pass 
    
    @abstractmethod
    def suspend(self, vm: 'VM') -> None:
        """Suspend the VM"""
        pass

