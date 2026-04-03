class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def notify(self, event_name, event_data):
        if event_name in self.listeners:
            for listener in self.listeners[event_name]:
                listener.update(event_data)