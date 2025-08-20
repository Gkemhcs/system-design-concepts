from observer import Observer,UptimeAlert

class UptimeService:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def unregister_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, alert: UptimeAlert):
        for observer in self._observers:
            observer.update(alert)
