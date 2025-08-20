package cor

import (
	"errors"
	"fmt"
)

func NewSecurityCheckHandler(next Handler) *SecurityCheckHandler {
	handler := &SecurityCheckHandler{}
	handler.SetNext(next)
	return handler
}

type SecurityCheckHandler struct {
	BaseHandler
}

func (h *SecurityCheckHandler) Handle(request *DeploymentRequest) error {
	if !request.PackageSecure {
		fmt.Printf("Security check failed for service %s\n", request.ServiceName)
		return errors.New("security check failed")
	}
	fmt.Printf("Security check passed for service %s\n", request.ServiceName)
	return h.CallNext(request)
}
