from django.conf.urls import url

from . import views

app_name = 'main_page'

urlpatterns = [
    url(r'^new/$', views.newMovie, name='new_movie'),
    url(r'^add/$', views.addMovie, name='add_movie'),
]
