'''
context processors allow you to have data available in your templates for every
request. It's important to be careful here since running DB queries every
request could be detrimental to your app's performance.
'''
from django.conf import settings

def settings_file_constants(request):
    return {
        'SITE_NAME': settings.SITE_NAME
    }
