from django.apps import AppConfig


class PsychologistsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'psychologists'

    def ready(self):
        import psychologists.signals