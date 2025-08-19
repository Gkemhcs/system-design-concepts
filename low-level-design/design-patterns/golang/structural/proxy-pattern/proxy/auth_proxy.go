package proxy

import "errors"

func NewAuthProxy(next ServiceHandler) *AuthProxy {
	return &AuthProxy{
		next: next,
	}
}

type AuthProxy struct {
	next ServiceHandler
}

func (a *AuthProxy) HandleRequest(request Request) (string, error) {
	// Implement authentication logic here
	if request.User_ID == "" {
		return "", errors.New("Unauthorized")
	}
	if request.Role != "admin" {
		return "", errors.New("access denied: insufficient permissions")

	}
	return a.next.HandleRequest(request)
}
