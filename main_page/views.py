from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Movie
from . import parser_filmweb

# Create your views here.

def newMovie(request):
    if 'fromFilmweb' in request.session:
        del request.session['fromFilmweb']
        movie = Movie()
        movie.org_title = request.session['org_title']
        print "org_title: ", movie.org_title
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
    return HttpResponse("Dodano film.")

def getFilmwebData(request):
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
    return HttpResponseRedirect(reverse('main_page:new_movie'))

def doAction(request):
    if 'newMovieFromFilmweb' in request.POST:
        return getFilmwebData(request)
    elif 'addNewMovie' in request.POST:
        return addMovie(request)