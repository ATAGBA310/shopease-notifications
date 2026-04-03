from src.channels.notification_channel import NotificationChannel


class SmsChannel(NotificationChannel):
    def send(self, recipient, message):
        print(f"[SMS] To: {recipient} | Message: {message}")