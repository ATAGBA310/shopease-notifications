from src.channels.notification_channel import NotificationChannel


class InternalChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"[INTERNAL] To: {recipient} | Message: {message}")