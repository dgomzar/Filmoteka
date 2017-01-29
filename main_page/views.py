from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Movie
from . import parser_filmweb

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'main_page/index.html'
    context_object_name = 'movies'
    def get_queryset(self):
        return Movie.objects.order_by('org_title')


def new_movie(request):
    if 'fromFilmweb' in request.session:
        del request.session['fromFilmweb']
        movie = Movie()
        set_up_essential_movie_data(movie, request.session)
        return render(request, 'main_page/new_movie.html', {'movie': movie})
    return render(request, 'main_page/new_movie.html')


def add_movie(request):
    movie = Movie()
    set_up_essential_movie_data(movie, request.POST)
    movie.save()
    return HttpResponseRedirect(reverse('main_page:view_movie', args=(movie.pk,)))


def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    set_up_essential_movie_data(movie, request.POST)
    movie.save()
    return HttpResponseRedirect(reverse('main_page:view_movie', args=(movie.pk,)))


def get_filmweb_data(request, pk):
    org_title = request.POST['org_title']
    movie = parser_filmweb.get_movie_from_filmweb(org_title)
    request.session['org_title'] = movie.org_title
    request.session['title'] = movie.title
    request.session['director'] = movie.director
    request.session['writer'] = movie.writer
    request.session['genres'] = movie.genres
    request.session['producer'] = movie.producer
    request.session['release_year'] = movie.release_year
    request.session['description'] = movie.description
    request.session['filmweb_rate'] = movie.rate
    request.session['fromFilmweb'] = True
    if pk == '0':
        return HttpResponseRedirect(reverse('main_page:new_movie'))
    else:
        return HttpResponseRedirect(reverse('main_page:edit_movie', args=(pk,)))


def do_action(request, pk):
    if 'newMovieFromFilmweb' in request.POST:
        return get_filmweb_data(request, pk)
    elif 'addNewMovie' in request.POST:
        return add_movie(request)
    elif 'updateMovie' in request.POST:
        return update_movie(request, pk)


class ViewMovie(generic.DetailView):
    model = Movie
    template_name = 'main_page/view_movie.html'


def remove_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return HttpResponseRedirect(reverse('main_page:index'))


def edit_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if 'fromFilmweb' in request.session:
        del request.session['fromFilmweb']
        set_up_essential_movie_data(movie, request.session)
    return render(request, 'main_page/edit_movie.html', {'movie' : movie})


def set_up_essential_movie_data(movie, container):
    movie.org_title = container['org_title']
    movie.title = container['title']
    movie.director = container['director']
    movie.writer = container['writer']
    movie.genres = container['genres']
    movie.producer = container['producer']
    movie.release_year = container['release_year']
    movie.description = container['description']
    movie.filmweb_rate = container['filmweb_rate']
