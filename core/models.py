from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text=''
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text=''
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
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

    def __str__(self):
        return f'GeneralSetting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This variable of the setting.', )

    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''

    )
    file = models.ImageField(
        default="",
        verbose_name='Image',
        help_text="",
        blank=True,
        upload_to='images/',
    )

    def __str__(self):
        return f'ImageSetting: {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text='This variable of the setting.',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        help_text='',
        validators=[MinValueValidator(0), MaxValueValidator(100)],

    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'
        ordering = ('order',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Company Name',
    )
    job_title = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Job Title',

    )
    job_location = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Job Location',

    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experience'
        ordering = ('start_date',)


class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='School_name',
    )
    major = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Major',

    )
    department = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Department',

    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Education: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('start_date',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    link = models.URLField(
        default="",
        max_length=255,
        blank=True,
        verbose_name='Link',

    )
    icon = models.CharField(
        default="",
        max_length=255,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return f'Social Media: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)
