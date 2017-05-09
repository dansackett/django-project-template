from django.conf import settings
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User
from accounts.forms import UserForm


def users_list(request):
    '''
    a list of users to operate on
    '''
    if not request.user.is_superuserish:
        return redirect('dashboard')
    users = User.objects.all()
    ctx = { 'users': users }
    return render(request, 'users_list.html', ctx)


def user_create(request):
    '''
    create a new user
    '''
    if not request.user.is_superuserish:
        return redirect('dashboard')
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return redirect('user-single', user.pk)
    ctx = { 'form': form }
    return render(request, 'user_create.html', ctx)


def user_single(request, pk):
    '''
    view a single user's page
    '''
    user = get_object_or_404(User, pk=pk)
    ctx = { 'this_user': user }
    return render(request, 'user_single.html', ctx)


def user_edit(request, pk):
    '''
    edit a single user
    '''
    user = get_object_or_404(User, pk=pk)
    if user.pk != request.user.pk or not request.user.is_superuserish:
        return redirect('dashboard')
    form = UserForm(request.POST or None, instance=user)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return redirect('user-single', user.pk)
    ctx = {
        'this_user': user,
        'form': form,
    }
    return render(request, 'user_edit.html', ctx)


@require_POST
def user_delete(request, pk):
    '''
    delete a single user
    '''
    user = get_object_or_404(User, pk=pk)
    if user.pk != request.user.pk or not request.user.is_superuserish:
        return redirect('dashboard')
    user.delete()
    return redirect('users-list')
