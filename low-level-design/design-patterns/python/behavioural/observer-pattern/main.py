from email_notifier import EmailNotifier
from slack_notifier import SlackNotifier
from dashboard_updater import DashboardUpdater
from uptime_service import UptimeService
from observer import UptimeAlert    


def main():

    email_notifier=EmailNotifier()
    slack_notifier=SlackNotifier()
    dashboard_updater=DashboardUpdater()

    uptime_service=UptimeService()

    uptime_service.register_observer(email_notifier)
    uptime_service.register_observer(slack_notifier)
    uptime_service.register_observer(dashboard_updater)

    uptime_service.notify(UptimeAlert("billing-service"))

    uptime_service.unregister_observer(email_notifier)
    uptime_service.notify(UptimeAlert("billing-service"))


if __name__=="__main__":
    main()

