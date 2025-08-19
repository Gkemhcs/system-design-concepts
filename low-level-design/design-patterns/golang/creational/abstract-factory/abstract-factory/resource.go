package abstractfactory

type Compute interface {
	Start() error 
	Stop() error
}

type Storage interface {

	Create(bucketName string )error 
}

type Network interface {

	Configure(name string ) error
}





