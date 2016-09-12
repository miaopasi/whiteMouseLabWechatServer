from django.conf.urls import url

from . import views

from .views import IndexView

urlpatterns = [
    # ex: /blacklist/
    url(r'^$', IndexView.as_view(), name='Black-List'),
    # ex: /blacklist/1/
    url(r'^(?P<shop_id>[0-9]+)/$', views.detail, name='detail'),
]