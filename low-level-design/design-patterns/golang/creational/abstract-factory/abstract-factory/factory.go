package abstractfactory



type Factory interface{
	CreateCompute() Compute
	CreateStorage() Storage
	CreateNetwork() Network
}