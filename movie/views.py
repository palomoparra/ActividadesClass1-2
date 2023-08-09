from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home (request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    return render(request, 'home.html', {'name':'Daniel Palomo'})

def about(request):
    return render(request, 'about.html')

def movie(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movie = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movie = Movie.objects.all()
    return render(request, 'Movie.html', {'searchTerm': searchTerm, 'movies': movie})