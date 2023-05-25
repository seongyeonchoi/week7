from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from django.utils import timezone

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    count = len(movies)
    ctx = {
        'movies': movies,
        'count' : count,
    }
    return render(request, 'home.html', ctx)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})

def create(request):
    if request.method == 'POST':
        movie = Movie()
        movie.title = request.POST['title']
        movie.r_rate = float(request.POST['r_rate'])
        movie.status = True if request.POST.get('status', None) == 'on' else False
        movie.review = request.POST['review']
        movie.save()
        return redirect('detail', movie.id)
    return render(request, 'create.html')

def comment(request, movie_id):
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.movie = get_object_or_404(Movie, pk=movie_id)
        new_comment.comment = request.POST['comment']
        new_comment.created_at = timezone.now()
        new_comment.save()
    return redirect('detail', movie_id)

def edit(request,id):
    edit_movie= Movie.objects.get(id=id)
    return render(request, 'edit.html', {'movie':edit_movie})

def update(request, id):
    update_movie= Movie.objects.get(id=id)
    update_movie.title= request.POST['title']
    update_movie.r_rate= request.POST['r_rate']
    update_movie.status= request.POST['status']
    update_movie.pub_date= timezone.now()
    update_movie.save()
    return redirect('detail', update_movie.id)

def delete(request, id):
    delete_movie= Movie.objects.get(id=id)
    delete_movie.delete()
    return redirect('home')