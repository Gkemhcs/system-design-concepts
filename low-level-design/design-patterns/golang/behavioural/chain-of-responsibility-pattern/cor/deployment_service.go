package cor

func NewDeploymentService(handler Handler) *DeploymentService {
	return &DeploymentService{
		handler: handler,
	}
}

type DeploymentService struct {
	handler Handler
}

func (h *DeploymentService) Deploy(request *DeploymentRequest) error {
	return h.handler.Handle(request)
}
