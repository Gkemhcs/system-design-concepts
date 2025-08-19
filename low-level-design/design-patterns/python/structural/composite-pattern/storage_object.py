from storage_resource import StorageResource

class StorageObject(StorageResource):
    def __init__(self, name: str, size: int):
        self.name = name
        self._size = size

    def create(self) -> None:
        print(f"Creating storage object: {self.name}")

    def delete(self) -> None:
        print(f"Deleting storage object: {self.name}")

    def count(self) -> int:
        return 1

    def size(self) -> int:
        return self._size