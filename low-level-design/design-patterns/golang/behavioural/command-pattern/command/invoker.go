package command

func NewInvoker() *Invoker {
	return &Invoker{}
}

type Invoker struct {
}

func (invoker *Invoker) ExecuteCommand(command Command) {
	if command == nil {
		return
	}
	command.Execute()
}
