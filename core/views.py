from django.conf import settings
from django.shortcuts import render

from accounts.models import User


def dashboard(request):
    '''
    placeholder dashboard display
    '''
    return render(request, 'dashboard_home.html',{})
