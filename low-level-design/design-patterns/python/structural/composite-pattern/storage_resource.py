from abc import ABC, abstractmethod

class StorageResource(ABC):
    @abstractmethod
    def create(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def size(self) -> int:
        pass