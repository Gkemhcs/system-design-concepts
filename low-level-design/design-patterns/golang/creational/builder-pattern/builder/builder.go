package builder

import "fmt"

func NewVMBuilder(name string) *VMBuilder {
	return &VMBuilder{
		vm: &VMResource{
			Name:     name,
			BootDisk: "default",
		},
	}

}

type VMBuilder struct {
	vm *VMResource
}

func (b *VMBuilder) AddCPU(cnt int) *VMBuilder {
	fmt.Println("Adding CPU count:", cnt)
	b.vm.CPU += cnt
	return b
}
func (b *VMBuilder) AddMemory(size int) *VMBuilder {
	fmt.Println("Adding memory size:", size)
	b.vm.Memory += size
	return b
}

func (b *VMBuilder) AddDataDisk(disk string) *VMBuilder {
	fmt.Println("Adding data disk:", disk)
	b.vm.DataDisks = append(b.vm.DataDisks, disk)
	return b
}

func (b *VMBuilder) AddNetwork(network int) *VMBuilder {
	fmt.Println("Adding network:", network)
	b.vm.Network = network
	return b

}

func (b *VMBuilder) AddPublicIP() *VMBuilder {
	fmt.Println("Adding public IP")
	b.vm.PublicIP = true

	return b
}

func (b *VMBuilder) Build() *VMResource {
	fmt.Println("Building VM Resource:")
	fmt.Println("VM resource created")
	return b.vm
}
