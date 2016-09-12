from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blacklist/
    url(r'^$', views.index, name='index'),
    # ex: /blacklist/1/
    url(r'^(?P<shop_id>[0-9]+)/$', views.detail, name='detail'),
]