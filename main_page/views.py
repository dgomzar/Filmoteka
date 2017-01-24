from django.shortcuts import render
from .models import Movie

# Create your views here.

def newMovie(request):
    return render(request, 'main_page/new_movie.html')
