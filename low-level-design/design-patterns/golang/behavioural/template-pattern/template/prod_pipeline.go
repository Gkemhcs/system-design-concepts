package template

import "fmt"

func NewProdPipeline()*ProdPipeline{
	return &ProdPipeline{
		BasePipeline: NewBasePipeline(),
	}
}

type ProdPipeline struct {
	*BasePipeline
}

func(p *ProdPipeline) Deploy(){
	fmt.Println("Deploying to prod environment")
}

func(p *ProdPipeline) Notify(){
	fmt.Println("notifying the deployment to prod slack channel")
}

