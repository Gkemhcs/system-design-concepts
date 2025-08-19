package abstractfactory

func NewGCPFactory() *GCPFactory {

	return &GCPFactory{}
}

type GCPFactory struct {
}

func (f *GCPFactory) CreateCompute() Compute {
	return NewGCPCompute()
}

func (f *GCPFactory) CreateStorage() Storage {
	return NewGCPStorage()
}

func (f *GCPFactory) CreateNetwork() Network {

	return NewGCPNetwork()
}
