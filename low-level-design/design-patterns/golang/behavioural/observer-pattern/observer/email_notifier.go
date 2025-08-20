package observer

func NewEmailNotifier() *EmailNotifier {
	return &EmailNotifier{}
}

type EmailNotifier struct {
}

func (n *EmailNotifier) Update(alert UptimeAlert) error {
	// Logic to send email notification
	// For example, using a mail service to send an email about the alert
	// Here we just print to simulate sending an email
	println("Sending email notification for service:", alert.ServiceName)
	return nil
}
