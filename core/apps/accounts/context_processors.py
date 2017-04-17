# GroupLookupDict proxy the groups system into objects that
# the template system can understand.


class GroupLookupDict:
    def __init__(self, user):
        self.user = user

    def __repr__(self):
        return str([g.name for g in self.user.groups.all()])

    def __getitem__(self, group_name):
        return self.user.belongs_to_group(group_name)

    def __iter__(self):
        raise TypeError("GroupLookupDict is not iterable.")


def groups(request):
    '''
    If there is no 'user' attribute in the request, use AnonymousUser (from
    django.contrib.auth).
    '''
    if hasattr(request, 'user'):
        user = request.user
    else:
        from django.contrib.auth.models import AnonymousUser
        user = AnonymousUser()

    return { 'groups': GroupLookupDict(user) }
