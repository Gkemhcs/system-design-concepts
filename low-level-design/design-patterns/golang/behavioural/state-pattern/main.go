package main

import (
	"fmt"
	"state-pattern/state"
)

func handle(err error) {
	if err != nil {
		fmt.Printf("Error: %v\n", err)
	}
}
func main() {

	startingState := state.NewStartingState()
	frontendVM := state.NewVM("frontend", startingState)
	handle(frontendVM.Start())
	handle(frontendVM.Stop())
	handle(frontendVM.Stop())
	handle(frontendVM.Start()	)
	handle(frontendVM.Suspend())
}
