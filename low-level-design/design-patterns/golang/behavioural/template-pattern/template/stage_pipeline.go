package template

import "fmt"

func NewStagePipeline()*StagePipeline{
	return &StagePipeline{
		BasePipeline: NewBasePipeline(),
	}
}

type StagePipeline struct {
	*BasePipeline
}

func (p *StagePipeline) Deploy() {
	fmt.Println("deploying to stage environment")
}


func(p *StagePipeline) Notify(){
	fmt.Println("notifying the staging email channel")
}
