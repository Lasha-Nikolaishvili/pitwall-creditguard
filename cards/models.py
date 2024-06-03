from django.db import models
from django.utils.translation import gettext_lazy as _


class Card(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name=_('User'))
    title = models.CharField(_('Title'), max_length=100)
    censored_number = models.CharField(_('Censored Number'), max_length=16)
    is_valid = models.BooleanField(_('Is Valid'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return self.censored_number

    class Meta:
        verbose_name = _('Card')
        verbose_name_plural = _('Cards')
        ordering = ('-id',)
