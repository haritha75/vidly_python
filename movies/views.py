from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Movie

# Create your views here.
# create main page in app mention index name
def index(request):
  movies = Movie.objects.all() # to gell all list of movies
  # output = ",".join([m.title for m in movies])
  # # select * from movies_movie
  # Movie.objects.filter(release_year=1984)
  # # select * from movies_movie where
  # Movie.objects.get(id=1)
  return render(request,'movies/index.html',{'movies':movies})

  # return HttpResponse(output)

# to format our data we are using render model it rendel the data like html,json format
def detail(request,movie_id):
 
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request,"movies/detail.html",{"movie":movie})



  