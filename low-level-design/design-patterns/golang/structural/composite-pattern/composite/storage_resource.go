package composite

type StorageResource interface {
	Create()
	Delete()
	Count() int 
	Size() int
}