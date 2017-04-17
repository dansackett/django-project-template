# Groups and Permissions

Django does a good job of providing all you really need to make building an
authorization framework easy. This boilerplate provides basic functionality to
create your own groups and assign permissions to those groups in the UI.

## Permissions

Permissions allow you to set a rules that a user can pass or fail in order to
do things in your app. For example, a permission like `can_publish_post` could
be added to a `Blog` model. Any user with this permission could create new
posts and those without will not be allowed to.

There are multiple ways to work with permissions so let's first look at how to
create new permissions.

The first approach is very explicit and allows you to contain your permission
logic on the model itself. Given a model `Book` in an app called `catalog` we
can defined permissions like so:

```
class Book(models.Model):
    ...
    class Meta:
        ...
        permissions = (("can_mark_returned", "Set book as returned"),)
```

This will create the new permission for the model. However, there may be
instances where you want to programttically create permissions. For example
your app may allow admins to create a set of permissions for their app and then
apply those custom permissions to their users. To do this we would build a
permission like so:

```
from catalog.models import Book
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Book)
permission = Permission.objects.create(
    codename='can_mark_returned',
    name='Set book as returned',
    content_type=content_type,
)
```

In this case we can see that a permission needs to know the content_type that
it is associated with. Users can now create their own permission instances.

Both approaches work well and are likely useful in different circumstances. The
first is probably best if your app defines its permissions within the code and
doesn't allow a user to make their own. The latter of course caters to that
case of creating custom permissions from a UI. Either way, you can check
permissions the same way.

Django provides utilities for doing this in templates and views. In templates
we can do the following:

```
{% if perms.catalog.can_mark_returned %}
    <!-- We can mark a Book as returned. -->
{% endif %}
```

The `perms` object is available in all views and will relate to the current
user instance on the request. As you can see we could make a button visible to
users with this permission allowing them to mark the book as returned.

When working with views, we will likely want to make our API stronger by
ensuring permissions block unauthorized behavior. We can do so like so:

```
from django.contrib.auth.decorators import permission_required

@permission_required('catalog.can_mark_returned')
def my_view(request):
    ...
```

For class-based views we can do something similiar:

```
from django.contrib.auth.mixins import PermissionRequiredMixin

class MyView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_mark_returned'
    # Or multiple of permissions:
    permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
```

Having these checks in our template and our view gives us the comfort of
knowing that our API and UI are both going to keep anauthorized behavior to a
minimum.

One other way to check permissions for a user is by using the `has_perm()`
method. This can be used like so:

```
if request.user.has_perm('catalog.can_mark_returned'):
    ...
```

## Groups

Groups are essentially just a list of permissions. When a user is assigned to a
group then they are given all of the permissions for that group. Groups can be
created programatically or they can be created in this boilerplate by an admin
in the UI. In order to create a new group programatically:

```
from django.contrib.auth.models import Group
group_obj = Group(name="Admins")
group_obj.save()
```

You can then assign a user to a group by doing the following:

```
user.groups.add(group_obj)
```

There is a convenience method on this user model in the boilerplate which
allows you to check for a user's existence in a group as well:

```
# can be called with a string
user.belongs_to_group('Admins')

# can also be called with a Group object
user.belongs_to_group(group_obj)
```

In most cases it will make sense to check if a user has a given permission to
access something. Checking if a user is in a given group can be useful though
so I created an API similiar to the permissions checking in both views and
templates.

In a view you can use a decorator:

```
from accounts.decorators import group_required

@group_required('Admins')
def my_view(request):
    ...
```

You can also use the mixin for class-based views:

```
from accounts.mixins import GroupRequiredMixin

class MyView(GroupRequiredMixin, View):
    group_required = 'Admins'
    # Or multiple of permissions:
    group_required = ('Admins', 'Editors')

    group_denied_message = 'You are not in the correct group to do that'
```

A `groups` objects is included in your templates as well to check if a user is
in a given group just like checking a permission:

```
{% if groups.Admin %}
    ...
{% endif %}
```

Like I mentioned, in most cases it will be best to check a user based on a
given permission but in the case of an application where groups are the
deciding factor or you want to check a group of permissions easier then you can
do so with some of the extra items I defined here.
