from django.apps import AppConfig


class DirectMessagesConfig(AppConfig):
    name = 'direct_messages'

def ready(self):
        import direct_messages.signals  # Register signals to enable foreign key checks