from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "dynamic_report.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import dynamic_report.users.signals  # noqa: F401
        except ImportError:
            pass
