from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^upload/$', views.upload, name='upload'),
    url(r'^add/$', views.add, name='add'),
    # url(r'^download/(?P<file_name>\w+)/$', views.download, name='download'),
]