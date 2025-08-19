from storage_bucket import StorageBucket
from storage_object import StorageObject

def main():
    root = StorageBucket("root")
    folder1 = StorageBucket("folder1")
    folder2 = StorageBucket("folder2")
    folder3 = StorageBucket("folder3")
    file1 = StorageObject("file1.txt", 100)
    file2 = StorageObject("file2.txt", 200)
    file3 = StorageObject("file3.txt", 100)
    file4 = StorageObject("file4.txt", 200)
    file5 = StorageObject("file5.txt", 100)
    file6 = StorageObject("file6.txt", 200)

    root.add(folder1)
    root.add(folder2)
    folder1.add(file1)
    folder2.add(file2)
    folder3.add(file3)
    folder3.add(file4)
    folder3.add(file5)
    folder3.add(file6)
    folder1.add(folder3)

    root.create()
    root.delete()
    print(f"Total size: {root.size()}")
    print(f"Total count: {root.count()}")

if __name__ == "__main__":
    main()