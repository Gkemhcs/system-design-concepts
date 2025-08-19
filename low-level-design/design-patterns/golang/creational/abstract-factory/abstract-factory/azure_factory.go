package abstractfactory

func NewAzureFactory() *AzureFactory {
	return &AzureFactory{}
}

type AzureFactory struct {
}



func (f *AzureFactory) CreateCompute() Compute {
	return NewAzureCompute()
}

func (f *AzureFactory) CreateStorage() Storage {
	return NewAzureStorage()
}

func (f *AzureFactory) CreateNetwork() Network {
	return NewAzureNetwork()
}
