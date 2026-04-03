from src.channels.notification_channel import NotificationChannel


class EmailChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"[EMAIL] To: {recipient} | Message: {message}")