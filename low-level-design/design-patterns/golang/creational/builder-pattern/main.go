package main

import "builder-pattern/builder"

func main(){

	vmBuilder:=builder.NewVMBuilder("vm-1")
	vmBuilder.AddCPU(5).AddMemory(10).AddDataDisk("disk1").AddNetwork(2).AddPublicIP().Build()
}
