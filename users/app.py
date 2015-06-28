from django.apps import AppConfig

class UserAppConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals