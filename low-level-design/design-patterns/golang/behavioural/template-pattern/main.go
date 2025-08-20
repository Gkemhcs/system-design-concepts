package main

import (
	"template-pattern/template"
)

func main() {
	stagePipeline := template.NewStagePipeline()
	prodPipeline := template.NewProdPipeline()

	pipelineRunner := template.NewPipelineRunner(stagePipeline)
	pipelineRunner.Run(stagePipeline)
	pipelineRunner.SetPipeline(prodPipeline)
	pipelineRunner.Run(prodPipeline)

}
