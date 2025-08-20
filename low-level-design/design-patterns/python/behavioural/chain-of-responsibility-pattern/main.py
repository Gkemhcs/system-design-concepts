from deployment_handler import DeploymentHandler
from handler import DeploymentRequest
from quota_check_handler import QuotaCheckHandler
from security_check_handler import SecurityCheckHandler
from deployment_service import DeploymentService

def main():
    deployment_handler = DeploymentHandler()
    quota_check_handler = QuotaCheckHandler(deployment_handler)
    security_check_handler = SecurityCheckHandler(quota_check_handler)
    deployment_service = DeploymentService(security_check_handler)

    print("----------valid request------------")
    deployment_service.deploy(
        DeploymentRequest(serviceName="valid_service", cpu=5, memory=15, package_secure=True)
    )

    print("-------------insecure service--------")
    deployment_service.deploy(
        DeploymentRequest(serviceName="insecure_service", cpu=5, memory=15, package_secure=False)
    
    )
    print("--------quota exceeded----------")

    deployment_service.deploy(
        DeploymentRequest(serviceName="quota_exceeded_service", cpu=200
                          ))
    

if __name__=="__main__":
    main()