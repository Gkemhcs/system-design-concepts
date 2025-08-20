from observer import    Observer,UptimeAlert

class SlackNotifier(Observer):
    def __init__(self):
        pass

    def update(self,alert:UptimeAlert):
        print(f"sending slack notification for {alert.service_name}")