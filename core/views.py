from django.shortcuts import render
from core.models import GeneralSetting, ImageSetting


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title = GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_welcome = GeneralSetting.objects.get(name='about_myself_welcome').parameter
    about_myself_footer = GeneralSetting.objects.get(name='about_myself_footer').parameter
    # image
    header_logo = ImageSetting.objects.get(name='header_logo').file

    context = {'site_title': site_title,
               'site_keywords': site_keywords,
               'site_description': site_description,
               'home_banner_name': home_banner_name,
               'home_banner_title': home_banner_title,
               'home_banner_description': home_banner_description,
               'about_myself_welcome': about_myself_welcome,
               'about_myself_footer': about_myself_footer,
               'header_logo': header_logo,

               }
    return render(request, 'index.html', context=context)
