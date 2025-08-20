from handler import BaseHandler,Handler,DeploymentRequest

class QuotaCheckHandler(BaseHandler):
    def __init__(self,handler:Handler):
        self.set_next(handler)
    
    def handle(self,request:DeploymentRequest):
        if request.cpu>10 or request.memory>20:
            print("QuotaCheckHandler: Request exceeds quota. Denying deployment.")
            return False
        print("QuotaCheckHandler: Quota check passed. Proceeding to next handler.")
        return self.call_next(request)
