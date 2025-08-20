from abc import ABC,abstractmethod

class BasePipeline(ABC):

    def run(self):
        self.test()
        self.build()
        self.deploy()
        self.notify()
    def test(self):
        print("running unit and integration tests")
    def build(self):
        print("building and pushing the docker image")
    
    @abstractmethod
    def deploy(self):
        pass 
    @abstractmethod
    def notify(self):
        pass 
