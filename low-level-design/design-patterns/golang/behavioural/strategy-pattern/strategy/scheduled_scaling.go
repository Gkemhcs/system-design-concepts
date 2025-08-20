package strategy

import "fmt"

func NewScheduledScaling() *ScheduledScaling {
	return &ScheduledScaling{}
}

type ScheduledScaling struct {
}

func (s *ScheduledScaling) ScaleUP(serviceName string) error {
	// Implement logic for scheduled scaling up
	fmt.Printf("\n  Scheduled scaling up %s \n", serviceName)
	return nil
}

func (s *ScheduledScaling) ScaleDown(serviceName string) error {
	// Implement logic for scheduled scaling down
	fmt.Printf("\n  Scheduled scaling down %s \n", serviceName)
	return nil
}
