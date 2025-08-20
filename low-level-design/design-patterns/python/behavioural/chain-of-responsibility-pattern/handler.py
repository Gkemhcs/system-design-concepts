from abc import ABC,abstractmethod

class DeploymentRequest:
    def __init__(self,serviceName,cpu=4,memory=16,package_secure=False):
        self.service_name=serviceName
        self.cpu=cpu
        self.memory=memory
        self.package_secure=package_secure


class Handler:    
   
   

    @abstractmethod
    def handle(self, request:DeploymentRequest):
      
        pass




class BaseHandler(Handler):
  

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def call_next(self, request:DeploymentRequest):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None
