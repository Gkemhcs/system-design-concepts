package adapter

import "fmt"

func NewGCPAdaptee()*GCPAdaptee{
	return &GCPAdaptee{}
}
type GCPAdaptee struct {
	
}


func(a *GCPAdaptee) PutObject(bucketName, filename string)error {
	fmt.Printf("\n uploading  %s to gcp bucket %s \n",filename, bucketName)
	return nil
}

func(a *GCPAdaptee) GetObject(bucketName, filename string)error {
	fmt.Printf("\n downloading  %s from gcp bucket %s \n",filename, bucketName)
	return nil
}