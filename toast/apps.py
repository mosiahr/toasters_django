from django.apps import AppConfig


class ToastConfig(AppConfig):
    name = 'toast'

    def ready(self):
        from . import signals