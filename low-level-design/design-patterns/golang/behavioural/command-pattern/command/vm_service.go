package command

import "fmt"

func NewVMService() *VMService {

	return &VMService{}
}

type VMService struct {
}

func (s *VMService) Create(name string) {
	fmt.Printf("vm named %s created\n", name)
}

func (s *VMService) Delete(name string) {
	fmt.Printf("vm named %s deleted\n", name)
}
