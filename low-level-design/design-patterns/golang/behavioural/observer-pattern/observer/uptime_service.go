package observer

type UptimeService struct {
	observers []Observer
}

func NewUptimeService() *UptimeService {
	return &UptimeService{}
}

func (s *UptimeService) RegisterObserver(observer Observer) {
	s.observers = append(s.observers, observer)
}

func (s *UptimeService) UnregisterObserver(observer Observer) {
	index := -1
	for i, o := range s.observers {
		if o == observer {
			index = i
			break
		}
	}
	if index != -1 {
		s.observers = append(s.observers[:index], s.observers[index+1:]...)
	}
}
func (s *UptimeService) Notify(alert UptimeAlert) {
	for _, observer := range s.observers {
		observer.Update(alert)
	}
}
