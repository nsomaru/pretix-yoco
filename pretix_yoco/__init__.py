from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = '1.0.0'


class PluginApp(PluginConfig):
    name = 'pretix_yoco'
    verbose_name = 'Pretix Yoco Payments'

    class PretixPluginMeta:
        name = gettext_lazy('Pretix Yoco Payments')
        author = 'Nikhil Somaru'
        description = gettext_lazy('A Pretix plugin to handle Yoco payment provider (South Africa)')
        visible = True
        version = __version__
        category = 'PAYMENT'
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_yoco.PluginApp'
