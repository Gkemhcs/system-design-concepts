package main

import "singleton-pattern/singleton"

func main() {

	logger1 := singleton.GetInstance()
	logger2 := singleton.GetInstance()
	logger1.Log("This is a log message.")
	logger2.Log("This is a log message.")
}
