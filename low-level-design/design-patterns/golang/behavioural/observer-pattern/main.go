package main

import "observer-pattern/observer"

func main() {

	dashboardUpdater := observer.NewDashboardUpdater()
	emailNotifier := observer.NewEmailNotifier()
	slackNotifier := observer.NewSlackNotifier()
	uptimeService := observer.NewUptimeService()

	uptimeService.RegisterObserver(dashboardUpdater)
	uptimeService.RegisterObserver(emailNotifier)
	uptimeService.RegisterObserver(slackNotifier)

	// Simulate an uptime alert
	alert := observer.UptimeAlert{
		ServiceName: "billing-service",
	}

	uptimeService.Notify(alert)

	uptimeService.UnregisterObserver(emailNotifier)

	uptimeService.Notify(alert)

}
