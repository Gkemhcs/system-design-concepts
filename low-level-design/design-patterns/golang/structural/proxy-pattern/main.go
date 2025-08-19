package main

import (
	"fmt"
	"proxy-pattern/proxy"
)

func main() {
	queryService := proxy.NewQueryService()

	cacheProxy := proxy.NewCacheProxy(queryService)
	rateLimiterProxy := proxy.NewRateLimiterProxy(cacheProxy, 2)
	authProxy := proxy.NewAuthProxy(rateLimiterProxy)
	client := proxy.NewQueryClient(authProxy)

	_, err := client.Query(proxy.Request{Query: "ping"})
	if err != nil {
		fmt.Println("Error:", err)

	}
	response, err := client.Query(proxy.Request{Query: "ping", User_ID: "i23j", Role: "admin"})
	if err != nil {
		fmt.Println("Error:", err)

	} else {
		fmt.Println("Response:", response)
	}

	response, err = client.Query(proxy.Request{Query: "ping", User_ID: "i23j", Role: "admin"})
	if err != nil {
		fmt.Println("Error:", err)
		return
	} else {
		fmt.Println("Response:", response)
	}

	response, err = client.Query(proxy.Request{Query: "ping", User_ID: "i23j", Role: "admin"})
	if err != nil {
		fmt.Println("Error:", err)
		return
	} else {
		fmt.Println("Response:", response)
	}

}
