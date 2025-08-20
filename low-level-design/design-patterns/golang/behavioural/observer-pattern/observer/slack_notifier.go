package observer

func NewSlackNotifier() *SlackNotifier {
	return &SlackNotifier{}
}

type SlackNotifier struct {
}

func (n *SlackNotifier) Update(alert UptimeAlert) error {
	// Logic to send alert to Slack
	// For example, using a Slack API client to post a message
	// Here we just print the alert for demonstration purposes
	println("Sending slack notification for service:", alert.ServiceName)
	return nil
}
