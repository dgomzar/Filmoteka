from django.conf.urls import url

from . import views

app_name = 'main_page'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.newMovie, name='new_movie'),
    url(r'^add/$', views.addMovie, name='add_movie'),
    url(r'^view/(?P<pk>[0-9]+)/$', views.ViewMovie.as_view(), name='view_movie'),
    url(r'^remove/(?P<pk>[0-9]+)/$', views.removeMovie, name='remove_movie'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.editMovie, name='edit_movie'),
    url(r'^do/(?P<pk>[0-9]+)/$', views.doAction, name='do_action'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.updateMovie, name='update_movie'),

]
