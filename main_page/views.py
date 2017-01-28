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


def newMovie(request):
    if 'fromFilmweb' in request.session:
        del request.session['fromFilmweb']
        movie = Movie()
        movie.org_title = request.session['org_title']
        movie.title = request.session['title']
        movie.director = request.session['director']
        movie.writer = request.session['writer']
        movie.genres = request.session['genres']
        movie.producer = request.session['producer']
        movie.release_year = request.session['release_year']
        movie.description = request.session['description']
        movie.filmweb_rate = request.session['filmweb_rate']
        return render(request, 'main_page/new_movie.html', {'movie': movie})
    return render(request, 'main_page/new_movie.html')


def addMovie(request):
    newMovie = Movie()
    newMovie.org_title = request.POST['org_title']
    newMovie.title = request.POST['title']
    newMovie.director = request.POST['director']
    newMovie.writer = request.POST['writer']
    newMovie.genres = request.POST['genres']
    newMovie.producer = request.POST['producer']
    newMovie.release_year = request.POST['release_year']
    newMovie.description = request.POST['description']
    newMovie.filmweb_rate = request.POST['filmweb_rate']
    newMovie.save()
    return HttpResponseRedirect(reverse('main_page:view_movie', args=(newMovie.pk,)))


def updateMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.org_title = request.POST['org_title']
    movie.title = request.POST['title']
    movie.director = request.POST['director']
    movie.writer = request.POST['writer']
    movie.genres = request.POST['genres']
    movie.producer = request.POST['producer']
    movie.release_year = request.POST['release_year']
    movie.description = request.POST['description']
    movie.filmweb_rate = request.POST['filmweb_rate']
    movie.save()
    return HttpResponseRedirect(reverse('main_page:view_movie', args=(movie.pk,)))


def getFilmwebData(request, pk):
    org_title = request.POST['org_title']
    movie = parser_filmweb.getMovieFromFilmweb(org_title)
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


def doAction(request, pk):
    if 'newMovieFromFilmweb' in request.POST:
        return getFilmwebData(request, pk)
    elif 'addNewMovie' in request.POST:
        return addMovie(request)
    elif 'updateMovie' in request.POST:
        return updateMovie(request, pk)


class ViewMovie(generic.DetailView):
    model = Movie
    template_name = 'main_page/view_movie.html'


def removeMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return HttpResponseRedirect(reverse('main_page:index'))

def editMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if 'fromFilmweb' in request.session:
        del request.session['fromFilmweb']
        movie.org_title = request.session['org_title']
        movie.title = request.session['title']
        movie.director = request.session['director']
        movie.writer = request.session['writer']
        movie.genres = request.session['genres']
        movie.producer = request.session['producer']
        movie.release_year = request.session['release_year']
        movie.description = request.session['description']
        movie.filmweb_rate = request.session['filmweb_rate']
    return render(request, 'main_page/edit_movie.html', {'movie' : movie})
