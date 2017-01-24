from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def newMovie(request):
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