from observer import Observer,UptimeAlert

class DashboardUpdater(Observer):
    def __init__(self):
        pass

    def update(self,alert:UptimeAlert):
        print(f"updating dashboard for {alert.service_name}")