package proxy

import "errors"

func NewQueryService() *QueryService {
	return &QueryService{
		data: map[string]string{
			"ping": "pong",
			"foo":  "bar",
			"baz":  "qux",
		},
	}

}

type QueryService struct {
	data map[string]string
}

func (s *QueryService) HandleRequest(request Request) (string, error) {
	if value, found := s.data[request.Query]; found {
		return value, nil
	}
	return "", errors.New("not found")
}
