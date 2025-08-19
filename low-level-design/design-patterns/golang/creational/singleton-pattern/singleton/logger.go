package singleton

import (
	"fmt"
	"log"
	"sync"
)

type SingletonLogger struct {
}

var instance *SingletonLogger
var mu sync.Mutex

func GetInstance() *SingletonLogger {
	mu.Lock()
	defer mu.Unlock()
	if instance == nil {
		fmt.Println("logger instance created")
		instance = &SingletonLogger{}
	}
	return instance
}

func (l *SingletonLogger) Log(message string) {
	log.Println(message)
}
