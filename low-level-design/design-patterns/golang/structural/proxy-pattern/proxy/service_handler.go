package proxy

type ServiceHandler interface {
	HandleRequest(request Request) (string, error)
}

type Request struct {
	User_ID string

	Query string
	Role  string
}
