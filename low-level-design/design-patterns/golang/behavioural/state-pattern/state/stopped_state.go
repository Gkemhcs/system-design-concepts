package state

import (
	"errors"
	"fmt"
)

func NewStoppedState() *StoppedState {
	return &StoppedState{}
}

type StoppedState struct {
}

func (s *StoppedState) Start(vm *VM) error {
	fmt.Printf(" starting the vm %s \n", vm.name)
	vm.SetState(NewStartingState())
	return nil
}
func (s *StoppedState) Stop(vm *VM) error {
	fmt.Printf(" %s vm is already stopped \n", vm.name)
	return errors.New("vm is already stopped")
}
func (s *StoppedState) Restart(vm *VM) error {
	fmt.Printf(" restarting the vm %s \n", vm.name)
	vm.SetState(NewStartingState())
	return nil
}
func (s *StoppedState) Suspend(vm *VM) error {
	fmt.Printf(" %s cannot suspend the vm as it is already stopped \n", vm.name)
	return errors.New("cannot suspend the vm as it is already stopped")
}

func (s *StoppedState) GetName() string {
	return "Stopped"
}
