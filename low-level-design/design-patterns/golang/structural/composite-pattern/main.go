package main

import (
	"composite-pattern/composite"
	"fmt"
)

func main() {
	root := composite.NewStorageBucket("root")
	folder1 := composite.NewStorageBucket("folder1")
	folder2 := composite.NewStorageBucket("folder2")
	folder3 := composite.NewStorageBucket("folder3")
	file1 := composite.NewStorageObject("file1.txt", 100)
	file2 := composite.NewStorageObject("file2.txt", 200)
	file3 := composite.NewStorageObject("file3.txt", 100)
	file4 := composite.NewStorageObject("file4.txt", 200)
	file5 := composite.NewStorageObject("file5.txt", 100)
	file6 := composite.NewStorageObject("file6.txt", 200)

	root.Add(folder1)
	root.Add(folder2)
	folder1.Add(file1)
	folder2.Add(file2)
	folder3.Add(file3)
	folder3.Add(file4)
	folder3.Add(file5)
	folder3.Add(file6)
	folder1.Add(folder3)

	root.Create()
	root.Delete()
	fmt.Printf("Total size: %d\n", root.Size())
	fmt.Printf("Total count: %d\n", root.Count())
}
