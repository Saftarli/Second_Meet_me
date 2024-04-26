from django.db import models


# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameter = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Parameter',
        help_text=''
    )
    updated_data = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text=''
    )
    created_data = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text=''
    )
    def __str__(self):
        return f'GeneralSetting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)
