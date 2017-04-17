from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import ImproperlyConfigured

from accounts.exceptions import GroupDenied


class GroupRequiredMixin(AccessMixin):
    '''
    verify that the current user is in a specified group
    '''
    group_required = None
    group_denied_message = ''

    def get_group_required(self):
        '''
        override this method to override the permission_required attribute.
        Must return an iterable.
        '''
        if self.group_required is None:
            raise ImproperlyConfigured(
                '{0} is missing the group_required attribute. Define {0}.group_required, or override '
                '{0}.get_group_required().'.format(self.__class__.__name__)
            )
        if isinstance(self.group_required, str):
            groups = (self.group_required, )
        else:
            groups = self.group_required
        return groups

    def has_group(self):
        '''
        Override this method to customize the way groups are checked.
        '''
        groups = self.get_group_required()
        return all(self.request.user.belongs_to_group(g) for g in groups)

    def get_group_denied_message(self):
        '''
        Override this method to override the permission_denied_message attribute.
        '''
        return self.group_denied_message

    def handle_no_group(self):
        if self.raise_exception:
            raise GroupDenied(self.get_group_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

    def dispatch(self, request, *args, **kwargs):
        if not self.has_group():
            return self.handle_no_group()
        return super().dispatch(request, *args, **kwargs)
