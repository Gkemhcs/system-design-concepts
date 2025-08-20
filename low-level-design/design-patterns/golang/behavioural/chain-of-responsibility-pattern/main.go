package main

import (
	"cor-pattern/cor"
	"fmt"
)

func main() {

	deploymentHandler := cor.NewDeploymentHandler()
	quotaCheckHandler := cor.NewQuotaCheckHandler(deploymentHandler)
	securityCheckHandler := cor.NewSecurityCheckHandler(quotaCheckHandler)
	deploymentService := cor.NewDeploymentService(securityCheckHandler)

	//valid request

	fmt.Println("------valid service------")
	deploymentService.Deploy(
		&cor.DeploymentRequest{
			ServiceName:   "valid-service",
			PackageSecure: true,
			Critical:      false,
		},
	)

	// insecure service

	fmt.Println("-------insecure service-------")
	deploymentService.Deploy(
		&cor.DeploymentRequest{
			ServiceName:   "malicious-service",
			PackageSecure: false,
			Critical:      false,
		},
	)
	fmt.Println("-------exceeded quota service-------")
	//Quota exceeded service request
	deploymentService.Deploy(
		&cor.DeploymentRequest{
			ServiceName:   "exceeed-quota-service",
			PackageSecure: true,
			Critical:      false,
			CPU:           2000,
		},
	)

}
