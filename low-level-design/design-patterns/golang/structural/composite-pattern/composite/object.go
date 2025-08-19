package composite

import "fmt"

func NewStorageObject(name string, size int) *StorageObject {
	return &StorageObject{
		name: name,
		size: size,
	}
}

type StorageObject struct {
	name string
	size int
}

func (s *StorageObject) Create() {
	// Implementation for creating a storage object
	fmt.Printf("Creating storage object: %s\n", s.name)
}

func (s *StorageObject) Delete() {
	// Implementation for deleting a storage object
	fmt.Printf("Deleting storage object: %s\n", s.name)
}

func (s *StorageObject) Count() int {
	// Implementation for counting storage objects
	return 1
}

func (s *StorageObject) Size() int {
	return s.size
}
