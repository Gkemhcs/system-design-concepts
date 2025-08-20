package command

import "fmt"

func NewStorageService() *StorageService {
	return &StorageService{}
}

type StorageService struct {
}

func (s *StorageService) Create(name string) {
	fmt.Printf("bucket named %s created\n", name)
}
func (s *StorageService) Delete(name string) {
	fmt.Printf("bucket named %s deleted\n", name)
}
