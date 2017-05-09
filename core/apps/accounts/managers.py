from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''
        creates and saves a User with the given email and password.
        '''
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        '''
        creates a non-admin user
        '''
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        '''
        creates an admin user and assigns them to the admin group
        '''
        admin_groups = Group.objects.filter(name=settings.ADMIN_GROUP_NAME)
        if not admin_groups:
            admin_group = Group(name=settings.ADMIN_GROUP_NAME)
            admin_group.save()
        else:
            admin_group = admin_groups.first()

        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        superuser = self._create_user(email, password, **extra_fields)
        superuser.groups.add(admin_group)
        return superuser
