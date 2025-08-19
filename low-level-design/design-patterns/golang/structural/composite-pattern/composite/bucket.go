package composite

import "fmt"

func NewStorageBucket(name string) *StorageBucket {
	return &StorageBucket{
		name:     name,
		children: []StorageResource{},
	}
}

type StorageBucket struct {
	name     string
	children []StorageResource
}

func (b *StorageBucket) Add(child StorageResource) {
	b.children = append(b.children, child)
}

func (b *StorageBucket) Create() {
	// Implementation for creating a storage bucket
	fmt.Printf("Creating storage bucket: %s\n", b.name)
	for _, child := range b.children {
		child.Create()
	}
}

func (b *StorageBucket) Delete() {
	fmt.Printf("Deleting storage bucket: %s\n", b.name)
	for _, child := range b.children {
		child.Delete()
	}
}

func(b *StorageBucket) Count() int {
	count := 0
	for _, child := range b.children {
		count += child.Count()
	}
	return count
}

func (b *StorageBucket) Size() int {
	count := 0
	for _, child := range b.children {
		count += child.Size()
	}
	return count	
}