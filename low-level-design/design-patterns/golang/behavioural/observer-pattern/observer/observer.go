package observer


type UptimeAlert struct {

	ServiceName string
}

type Observer interface {
	Update(alert UptimeAlert)error 
}