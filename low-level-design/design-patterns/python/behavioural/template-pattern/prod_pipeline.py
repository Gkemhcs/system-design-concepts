from pipeline_template import BasePipeline

class ProdPipeline(BasePipeline):

    def deploy(self):
        print("deploying to production environment")
    def notify(self):
        print("notifying the deployment to slack channels")
