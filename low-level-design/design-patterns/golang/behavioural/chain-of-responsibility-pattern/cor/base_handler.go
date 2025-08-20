package cor

type DeploymentRequest struct {
	ServiceName   string
	CPU           int               // Requested CPU units
	Memory        int               // Requested Memory units
	PackageSecure bool              // Security scan passed
	Critical      bool              // Requires manager approval
	Env           string            // Deployment environment: dev/staging/prod
	Tags          map[string]string // Optional metadata for policies
}

type Handler interface {
	SetNext(handler Handler)
	Handle(request *DeploymentRequest)error
}

type BaseHandler struct {
	next Handler
}

func (h *BaseHandler) SetNext(handler Handler) {
	h.next = handler
}
func (h *BaseHandler) CallNext(request *DeploymentRequest) error{
	if h.next != nil {
		return h.next.Handle(request)
	}
	return nil
}
