package strategy

import (
	"fmt"
)

func NewCPUThresholdScaling() *CPUThresholdScaling {
	return &CPUThresholdScaling{}
}

type CPUThresholdScaling struct {
}

func (s *CPUThresholdScaling) ScaleUP(serviceName string) error {
	fmt.Printf("\n  Scaling up %s as cpu threshold reached \n", serviceName)
	return nil
}

func (s *CPUThresholdScaling) ScaleDown(serviceName string) error {
	fmt.Printf("\n  Scaling down %s as cpu threshold not reached and resources are under utilized \n", serviceName)
	return nil
}
