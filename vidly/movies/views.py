from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Artist, Gallery, ArtWork
from .forms import ArtistForm


def index(request):
    artists = Artist.objects.all()
    return render(request, 'movies/index.html', {'artists': artists})


def detail(request, artist_id):
    m = get_object_or_404(Artist, id=artist_id)
    # return render(request, 'movies/detail.html', {'artist': m})

    form = ArtistForm()
    form.Name = m.Name
    form.Movement = m.Movement
    form.Born = m.Born
    form.Birthplace = m.Birthplace
    form.Death = m.Death

    return render(request, 'movies/add.html', {'form': form})

    # try:
    #     m = artist.objects.get(id=artist_id)
    #     return render(request, 'artists/detail.html', {'artist': m})
    # except artist.DoesNotExist:
    #     raise Http404


def add(request):
    form = ArtistForm()
    return render(request, 'movies/add.html', {'form': form})


def save_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            # form.save()
            a = Artist()
            a.Name = form.cleaned_data['Name']
            a.Birthplace = form.cleaned_data['Birthplace']
            a.Born = form.cleaned_data['Born']
            a.Death = form.cleaned_data['Death']
            a.Movement = form.cleaned_data['Movement']
            a.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            artists = Artist.objects.all()
            return render(request, 'movies/index.html', {'artists': artists})
    else:
        form = ArtistForm()
    return render(request, 'movies/add.html', {'form': form})


def delete(request, artist_id):
    m = get_object_or_404(Artist, id=artist_id)

    m.delete()
    artists = Artist.objects.all()
    return render(request, 'movies/index.html', {'artists': artists})


def edit(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    return render(request, 'movies/edit.html', {'artist': artist})


def update(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    print(request.POST)
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():

        print(form.cleaned_data)
        form.save()
        artists = Artist.objects.all()
        return render(request, 'movies/index.html', {'artists': artists})

    return render(request, 'movies/edit.html', {'artist': artist})
