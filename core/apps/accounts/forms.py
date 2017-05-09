from django import forms
from accounts.models import User


class UserForm(forms.ModelForm):
    '''
    standard user create and edit form
    '''
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar',)
