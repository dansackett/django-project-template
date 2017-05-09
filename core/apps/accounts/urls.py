from django.conf.urls import url

from accounts import views as account_views

urlpatterns = [
    url(r'users/$', account_views.users_list, name='users-list'),
    url(r'users/new/$', account_views.user_create, name='user-create'),
    url(r'user/(?P<pk>\d+)/$', account_views.user_single, name='user-single'),
    url(r'user/(?P<pk>\d+)/edit/$', account_views.user_edit, name='user-edit'),
    url(r'user/(?P<pk>\d+)/delete/$', account_views.user_delete, name='user-delete'),
]
