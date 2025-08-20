from handler import Handler,DeploymentRequest

class DeploymentService:
    def __init__(self, handler: Handler):
        self.handler = handler

    def deploy(self, request: DeploymentRequest):
        print(f"DeploymentService: Attempting to deploy {request.service_name}...")
        if self.handler.handle(request):
            print(f"DeploymentService: Successfully deployed {request.service_name}.")
            return True
        else:
            print(f"DeploymentService: Failed to deploy {request.service_name}.")
            return False