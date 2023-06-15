from django.apps import AppConfig


class AuthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auths'
    verbose_name: str = "Авторизация"

    def ready(self) -> None:
        import auths.signals  # noqa
