package proxy

import (
	"errors"
	"sync"
)

func NewRateLimiterProxy(next ServiceHandler, limit int) *RateLimiterProxy {
	return &RateLimiterProxy{
		limitPerUserMap: make(map[string]int),
		next:            next,
		limit:           limit,
		mu:              &sync.Mutex{},
	}
}

type RateLimiterProxy struct {
	limitPerUserMap map[string]int
	next            ServiceHandler
	limit           int
	mu              *sync.Mutex
}

func (proxy *RateLimiterProxy) HandleRequest(request Request) (string, error) {
	userID := request.User_ID
	proxy.mu.Lock()
	if _, found := proxy.limitPerUserMap[userID]; !found {
		proxy.limitPerUserMap[userID] = 0
	}
	if proxy.limitPerUserMap[userID] >= proxy.limit {
		proxy.mu.Unlock()
		return "", errors.New("rate limit exceeded")
	}
	proxy.limitPerUserMap[userID]++
	proxy.mu.Unlock()
	return proxy.next.HandleRequest(request)
}
