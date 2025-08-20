package template

import "fmt"

func NewBasePipeline() *BasePipeline {
	return &BasePipeline{}
}

type BasePipeline struct {
}

func (p *BasePipeline) Run(pipeline PipelineTemplate) {
	pipeline.Test()
	pipeline.Build()
	pipeline.Deploy()
	pipeline.Notify()

}

func (p *BasePipeline) Test() {
	fmt.Println("Running automation tests and deployment tests")
}
func (p *BasePipeline) Build() {
	fmt.Println("building  and pushing a docker image")
}
func (p *BasePipeline) Deploy() {
	fmt.Println("deploying the service using default configuration")

}

func (b *BasePipeline) Notify() {
	fmt.Println("notifying the default channels")
}
