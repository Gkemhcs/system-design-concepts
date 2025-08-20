from observer import Observer,UptimeAlert




class EmailNotifier(Observer):
    def __init(self):
        pass 
    
    def update(self,alert:UptimeAlert):
        print(f"sending email notification for {alert.service_name}")