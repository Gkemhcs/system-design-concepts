package strategy

type AutoScalingStrategy interface {
	ScaleUP(serviceName string) error
	ScaleDown(serviceName string) error
}
