package cor

import (
	"errors"
	"fmt"
)

func NewQuotaCheckHandler(next Handler) *QuotaCheckHandler {
	handler := &QuotaCheckHandler{}
	handler.SetNext(next)
	return handler
}

type QuotaCheckHandler struct {
	BaseHandler
}

func (h *QuotaCheckHandler) Handle(request *DeploymentRequest) error {
	if request.CPU > 1000 || request.Memory > 2048 {
		fmt.Printf("Quota exceeded for service %s: CPU %d, Memory %d\n", request.ServiceName, request.CPU, request.Memory)
		return errors.New("quota exceeded")
	}
	fmt.Print("Quota check passed\n")
	return h.CallNext(request)

}
