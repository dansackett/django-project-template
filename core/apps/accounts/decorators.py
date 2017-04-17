from django.contrib.auth.decorators import user_passes_test

from accounts.exceptions import GroupDenied

def group_required(group, login_url=None, raise_exception=False):
    '''
    decorator for views that checks whether a user is in a particular group,
    redirecting to the log-in page if necessary. If the raise_exception
    parameter is given the GroupDenied exception is raised.
    '''
    def check_group(user):
        # First check if the user is in the group
        if user.belongs_to_group(group):
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise GroupDenied
        # As the last resort, show the login form
        return False
    return user_passes_test(check_groups, login_url=login_url)
