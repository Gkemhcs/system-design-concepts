package template

type PipelineTemplate interface {
	Run(PipelineTemplate)
	Build()
	Test()
	Deploy()
	Notify()
}
