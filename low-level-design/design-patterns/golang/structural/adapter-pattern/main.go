package main

import (
	"adapter-pattern/adapter"
)

func main() {

	gcpAdapter := adapter.NewGCPAdapter()
	client := adapter.NewFrontendClient(gcpAdapter)
	client.UploadFile("file.txt")
	client.DownloadFile("file.txt")	

}
