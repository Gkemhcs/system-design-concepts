from handler import BaseHandler,Handler,DeploymentRequest

class DeploymentHandler(BaseHandler):
    def __init__(self):
        pass 
    
    def handle(self,request:DeploymentRequest):
        
        print(f"deployment is getting created for {request.service_name} ")
        return True
