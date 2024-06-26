# api/apps.py

from django.apps import AppConfig

class BackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'  # Asegúrate de que 'name' sea 'api'

    def ready(self):
        import api.signals