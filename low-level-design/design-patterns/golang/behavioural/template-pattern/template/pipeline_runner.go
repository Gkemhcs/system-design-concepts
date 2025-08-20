package template

func NewPipelineRunner(pipeline PipelineTemplate) *PipelineRunner {
	return &PipelineRunner{
		pipeline: pipeline,
	}
}

type PipelineRunner struct {
	pipeline PipelineTemplate
}

func (runner *PipelineRunner) SetPipeline(pipeline PipelineTemplate) {
	runner.pipeline = pipeline
}
func (runner *PipelineRunner) Run(pipeline PipelineTemplate) {
	runner.pipeline.Run(pipeline)
}
