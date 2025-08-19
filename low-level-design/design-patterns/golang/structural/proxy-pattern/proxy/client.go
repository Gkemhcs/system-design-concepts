package proxy


func NewQueryClient(service ServiceHandler) *QueryClient {
	return &QueryClient{
		service: service,
	}
}
type QueryClient struct {
	service ServiceHandler
}

func (client *QueryClient) Query(request Request) (string, error) {
	// Here we can add additional logic before sending the request
	return client.service.HandleRequest(request)
}