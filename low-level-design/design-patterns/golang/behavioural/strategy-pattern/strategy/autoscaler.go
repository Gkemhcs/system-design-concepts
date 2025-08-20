package strategy

func NewAutoScaler(strategy AutoScalingStrategy) *AutoScaler {
	return &AutoScaler{
		strategy: strategy,
	}
}

type AutoScaler struct {
	strategy AutoScalingStrategy
}

func (a *AutoScaler) ScaleUp(serviceName string) error {
	return a.strategy.ScaleUP(serviceName)
}
func (a *AutoScaler) ChangeStrategy(strategy AutoScalingStrategy) {

	a.strategy = strategy
}
func (a *AutoScaler) ScaleDown(serviceName string) error {
	return a.strategy.ScaleDown(serviceName)
}
