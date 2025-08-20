package main

import "strategy-pattern/strategy"

func main() {

	cpuScaler := strategy.NewCPUThresholdScaling()
	memoryScaler := strategy.NewMemoryThresholdScalingStrategy()
	scheduledScaler := strategy.NewScheduledScaling()

	autoScaler := strategy.NewAutoScaler(cpuScaler)
	autoScaler.ScaleUp("billing-service")
	autoScaler.ScaleDown("billing-service")
	autoScaler.ChangeStrategy(memoryScaler)
	autoScaler.ScaleUp("billing-service")
	autoScaler.ScaleDown("billing-service")
	autoScaler.ChangeStrategy(scheduledScaler)
	autoScaler.ScaleUp("billing-service")
	autoScaler.ScaleDown("billing-service")
}
