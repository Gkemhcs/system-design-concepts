package proxy

import (
	"fmt"
	"sync"
)

func NewCacheProxy(next ServiceHandler) *CacheProxy {
	return &CacheProxy{
		cache: make(map[string]string),
		next:  next,
		mu:    &sync.RWMutex{},
	}
}

type CacheProxy struct {
	cache map[string]string
	next  ServiceHandler
	mu    *sync.RWMutex
}

func (proxy *CacheProxy) HandleRequest(request Request) (string, error) {
	proxy.mu.RLock()
	response, found := proxy.cache[request.Query]
	proxy.mu.RUnlock()
	if found {
		fmt.Printf("%s found in cache  \n", request.Query)
		return response, nil
	}

	response, err := proxy.next.HandleRequest(request)
	if err != nil {
		return "", err
	}

	proxy.mu.Lock()
	proxy.cache[request.Query] = response
	proxy.mu.Unlock()
	return response, nil
}
