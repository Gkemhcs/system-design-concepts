package strategy

import "fmt"

func NewMemoryThresholdScalingStrategy() *MemoryThresholdScaling {
	return &MemoryThresholdScaling{}
}

type MemoryThresholdScaling struct {
}

func (s *MemoryThresholdScaling) ScaleUP(serviceName string) error {
	fmt.Printf("\n  Scaling up %s as memory threshold reached \n", serviceName)
	return nil
}

func (s *MemoryThresholdScaling) ScaleDown(serviceName string) error {
	fmt.Printf("\n  Scaling down %s as memory threshold not reached and resources are under utilized \n", serviceName)
	return nil
}
