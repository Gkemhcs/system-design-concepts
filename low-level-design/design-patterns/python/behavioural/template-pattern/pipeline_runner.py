from pipeline_template import BasePipeline


class PipelineRunner:

    @staticmethod
    def Run(pipeline:BasePipeline):
        pipeline.run()