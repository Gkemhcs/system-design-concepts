from storage_resource import StorageResource

class StorageBucket(StorageResource):
    def __init__(self, name: str):
        self.name = name
        self.children: list[StorageResource] = []

    def add(self, child: StorageResource) -> None:
        self.children.append(child)

    def create(self) -> None:
        print(f"Creating storage bucket: {self.name}")
        for child in self.children:
            child.create()

    def delete(self) -> None:
        print(f"Deleting storage bucket: {self.name}")
        for child in self.children:
            child.delete()

    def count(self) -> int:
        return sum(child.count() for child in self.children)

    def size(self) -> int:
        return sum(child.size() for child in self.children)