class NotificationListener:
    def __init__(self, channel, recipient, message_builder):
        self.channel = channel
        self.recipient = recipient
        self.message_builder = message_builder

    def update(self, event_data):
        message = self.message_builder(event_data)
        self.channel.send(self.recipient, message)