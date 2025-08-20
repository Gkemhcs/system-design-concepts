from  pipeline_template import BasePipeline

class StagePipeline(BasePipeline):

    def deploy(self):
        print("deploying to stage environment")
    def notify(self):
        print("notifying the deployment to email channels")