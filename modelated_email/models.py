from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .settings import BodyField


@python_2_unicode_compatible
class EmailTemplate(models.Model):
    """
    The model used to store the template email. Inspired from django oscar
    Code - used as identifier.
    Name - friendly description
    """
    code = models.SlugField(
        _('Code'), max_length=128, unique=True, editable=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z_][0-9a-zA-Z_]*$',
                message=_(
                    "Code can only contain the letters a-z, A-Z, digits, "
                    "and underscores, and can't start with a digit."))],
        help_text=_("Code used for looking up this event programmatically"))
    name = models.CharField(
        _('Name'), max_length=255,
        help_text=_("This is just used for organisational purposes"))
    subject = models.TextField(verbose_name=_('Subject'))
    body = BodyField(verbose_name=_('Body'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Email template")
        verbose_name_plural = _("Email templates")

