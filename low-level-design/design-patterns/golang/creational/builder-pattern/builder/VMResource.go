package builder

type VMResource struct {
	Name      string
	CPU       int
	Memory    int
	BootDisk  string
	Network   int
	DataDisks []string
	PublicIP  bool
}
