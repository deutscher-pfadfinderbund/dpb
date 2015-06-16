from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FlatPagesConfig(AppConfig):
    name = 'dpbflatpages'
    verbose_name = _("DPB Flat Pages")
