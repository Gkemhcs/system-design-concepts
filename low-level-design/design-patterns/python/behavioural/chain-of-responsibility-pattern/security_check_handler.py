from handler import BaseHandler,Handler,DeploymentRequest

class SecurityCheckHandler(BaseHandler):
    def __init__(self,handler:Handler):
        self.set_next(handler)
    
    def handle(self,request:DeploymentRequest):
        if not request.package_secure:
            print("SecurityCheckHandler: Package not secure. Denying deployment.")
            return False
        print("SecurityCheckHandler: Package security check passed. Proceeding to next handler.")
        return self.call_next(request)
