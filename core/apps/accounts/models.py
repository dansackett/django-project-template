from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, Group
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def get_display_name(self):
        '''
        get a readable name for the UI
        '''
        if self.get_full_name().strip():
            return self.get_full_name()
        elif self.get_short_name().strip():
            return self.get_short_name()
        return self.email

    def get_full_name(self):
        '''
        returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def belongs_to_group(self, group_or_name):
        '''
        determine if the user belongs to a given group by object or name
        '''
        name = group_or_name
        if isinstance(group_or_name, Group):
            name = group_or_name.name
        return Group.objects.filter(name=name).exists()
