package cor

import (
	"errors"
	"fmt"
)

func NewDeploymentHandler() *DeploymentHandler {
	return &DeploymentHandler{}
}

type DeploymentHandler struct {
	BaseHandler
}

func (h *DeploymentHandler) Handle(request *DeploymentRequest) error {
	if request.Critical {
		fmt.Printf("Critical deployment for service %s requires manager approval\n", request.ServiceName)
		return errors.New("critical deployment requires approval")
	}
	fmt.Printf("Deployment request for service %s is being processed\n", request.ServiceName)
	return nil
}
