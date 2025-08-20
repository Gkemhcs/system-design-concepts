package observer

func NewDashboardUpdater() *DashboardUpdater {
	return &DashboardUpdater{}
}

type DashboardUpdater struct {
}

func (u *DashboardUpdater) Update(alert UptimeAlert) error {
	// Logic to update the dashboard with the alert information
	// For example, updating a UI component or a database record
	// Here we just print to simulate updating the dashboard
	println("Updating dashboard for service:", alert.ServiceName)
	return nil
}
