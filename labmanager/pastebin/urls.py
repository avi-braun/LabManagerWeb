from django.conf.urls import *
from .models import Paste
from . import views
urlpatterns = [
    url(r'^$', 'django.views.generic.create_update.create_object', { 'model': Paste }),
]

    # url(r'^paste/(?P<object_id>\d+)$', 'django.views.generic.list_detail.object_detail',
    #     {'queryset': Paste.objects.all()}, name='pastebin_paste_detail'),
    #                    )
