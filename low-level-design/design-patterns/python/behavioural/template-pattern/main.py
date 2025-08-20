from pipeline_runner import PipelineRunner
from stage_pipeline import StagePipeline
from prod_pipeline import ProdPipeline


def main():
    prod_pipeline=ProdPipeline()
    stage_pipeline=StagePipeline()
    PipelineRunner.Run(prod_pipeline)
    PipelineRunner.Run(stage_pipeline)


if __name__=="__main__":
    main()      

