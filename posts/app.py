from django.apps import AppConfig

class PostAppConfig(AppConfig):
    name = 'posts'

    def ready(self):
        import posts.signals