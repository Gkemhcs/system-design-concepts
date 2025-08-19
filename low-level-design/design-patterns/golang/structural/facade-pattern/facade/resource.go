package facade

type NetworkManager interface {
	Create() error
	Delete() error
}

type BlockStorageManager interface {
	Create() error
	Delete() error
}

type VMManager interface {
	Create() error
	Delete() error
	Start() error
	Stop() error
}
