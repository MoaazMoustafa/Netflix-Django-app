from django.shortcuts import render, redirect
from .models import Movie
from django.http import HttpResponse
from .forms import MovieForm
from django.core.mail import send_mail
# Create your views here.


def movie_index(request):
    movies = Movie.objects.all()
    return render(request, "movies/movie_index.html", context={'movies': movies})
    # return HttpResponse("sdfadfjlakf")


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/movie_detail.html', context={'movie': movie})


def movie_create(request):
    form = MovieForm()
    print("REQUEST TYPE -> ", request.method)

    print(request.FILES)

    # POST REQUEST HANDLING
    if request.method == 'POST':

        form = MovieForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # send_mail('New Movie Created', f'Dear User {request.POST.get("name")}',
            #           'moaazmoustafa@gmail.com', ['moaazmoustafa@outlook.com'], fail_silently=False)
            form.save()
            return redirect('movie:movie-index')

    # GET REQUEST HANDLING
    return render(request, 'movies/movie_create.html', context={'form': form})


def movie_update(request, pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if request.method == 'POST':
        form = MovieForm(data=request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-detail', pk=movie.id)

    return render(request, 'movies/movie_update.html', context={'form': form, 'movie': movie})


def movie_delete(request, pk):
    Movie.objects.get(id=pk).delete()
    return redirect('movie:movie-index')
