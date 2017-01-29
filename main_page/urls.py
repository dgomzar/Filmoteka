from django.conf.urls import url

from . import views

app_name = 'main_page'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.new_movie, name='new_movie'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.ViewMovie.as_view(), name='view_movie'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.remove_movie, name='remove_movie'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.edit_movie, name='edit_movie'),
    url(r'^do/(?P<pk>[0-9]+)/$', views.do_action, name='do_action'),
]
