from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.users_list, name='users_list'),
    url(r'^(?P<username>[-\w]+)/$',
        views.user_details, name='user_details')
]