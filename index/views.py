from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.db.models import Q
from .models import Song, Ministry, SongMinistry
from .forms import SongForm, MinistrysForm
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    date = timezone.now().date()
    data = {
        'title': "Planning",
        'date': date
    }
    return render(request, 'index/index.html', data)

def songs(request):
    if not request.user.is_authenticated:
        return redirect('login')

    songs_objects = Song.objects.filter()
    paginator = Paginator(songs_objects, 25)
    page = request.GET.get('page', 1)

    has_permission = request.user.has_perm('songs.can_edit')

    try:
        songs = paginator.page(page)
    except PageNotAnInteger:
        songs = paginator.page(1)
    except EmptyPage:
        songs = paginator.page(paginator.num_pages)

    data = {
        'title': "Planning-songs",
        'has_permission': has_permission,
        'songs': songs
    }

    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        data_html = {
            'songs_html': render_to_string('songs/songs_ajax.html', data),
            'pagination_html': render_to_string('songs/pagination_ajax.html', data),
        }
        return JsonResponse(data_html)
    return render(request, 'songs/songs.html', data)

def search_songs(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        query = request.GET.get('q', '')
        songs_objects = Song.objects.filter(Q(name__icontains=query)) # | Q(text__icontains=query)
        paginator = Paginator(songs_objects, 25)
        page = request.GET.get('page', 1)

        try:
            songs = paginator.page(page)
        except PageNotAnInteger:
            songs = paginator.page(1)
        except EmptyPage:
            songs = paginator.page(paginator.num_pages)
        data = {
            'has_permission': request.user.has_perm('songs.can_edit'),
            'songs': songs,
            'query': query
        }
        data_html = {
            'songs_html': render_to_string('songs/songs_ajax.html', data),
            'pagination_html': render_to_string('songs/pagination_ajax.html', data),
        }
        return JsonResponse(data_html)

def song(request, song_id):
    if not request.user.is_authenticated:
        return redirect('login')
    song = Song.objects.get(id=song_id)
    choices = Song.KEYS
    has_permission = request.user.has_perm('songs.can_edit')
    data = {
        'title': f"Planning-{song.name}",
        'song': song,
        'choices': choices,
        'has_permission': has_permission
    }
    return render(request, 'songs/song.html', data)

@permission_required('songs.can_create', raise_exception=True)
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.save()
            if '_save' in request.POST:
                return redirect('songs')
            elif '_addanother' in request.POST:
                return redirect('upload_song')
            else:
                return redirect('edit_song')
    else:
        form = SongForm()
    data =  {
        'title': "Planning-upload song",
        'form': form
    }
    return render(request, 'songs/upload_song.html', data)

@permission_required('songs.can_edit', raise_exception=True)
def edit_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.save()
            if '_save' in request.POST:
                return redirect('songs')
            elif '_addanother' in request.POST:
                return redirect('upload_song')
            else:
                return redirect('edit_song')
    else:
        form = SongForm(instance=song)
    data = {
        'form': form,
        'song': song
    }
    return render(request, 'songs/edit_song.html', data)

@permission_required('ministrys.can_delete', raise_exception=True)
def delete_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.delete()
    data = {
        'title': f"Planning-{song.name}",
        'song': song
    }
    return render(request, 'songs/deleted.html', data)


def ministrys(request):
    if not request.user.is_authenticated:
        return redirect('login')
    current_date = datetime.now().date()
    has_permission = request.user.has_perm('ministrys.can_edit')
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if is_ajax:
        if request.GET.get('future') == 'false':
            ministrys = Ministry.objects.filter(date__gte=current_date)
        else:
            ministrys = Ministry.objects.filter(date__lt=current_date)
        data = {
            'ministrys': ministrys,
            'has_permission': has_permission,
        }
        data_html = {
            'ministrys_html': render_to_string('ministrys/ministrys_ajax.html', data)
        }
        return JsonResponse(data_html)

    ministrys = Ministry.objects.filter(date__gt=current_date)
    data = {
        'title': "Planning-ministrys",
        'ministrys': ministrys,
        'has_permission': has_permission,
    }
    return render(request, 'ministrys/ministrys.html', data)

def ministry(request, ministry_id):
    if not request.user.is_authenticated:
        return redirect('login')
    ministry = Ministry.objects.get(id=ministry_id)
    songs = SongMinistry.objects.filter(model=ministry)
    data = {
        'title': f"Planning-{ministry.name}",
        'ministry': ministry,
        'songs': songs
    }
    return render(request, 'ministrys/ministry.html', data)

@permission_required('ministrys.can_create', raise_exception=True)
def upload_ministry(request):
    if request.method == 'POST':
        form = MinistrysForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if '_save' in request.POST:
                return redirect('ministrys')
            elif '_addanother' in request.POST:
                return redirect('upload_ministry')
            else:
                return redirect('edit_ministry')
    else:
        form = MinistrysForm()
    data =  {
        'title': "Planning-upload song",
        'form': form
    }
    return render(request, 'ministrys/update/ministry.html', data)

@permission_required('ministrys.can_edit', raise_exception=True)
def edit_ministry(request, ministry_id):
    ministry = get_object_or_404(Ministry, id=ministry_id)

    if request.method == 'POST':
        form = MinistrysForm(request.POST, request.FILES, instance=ministry)
        if form.is_valid():
            form.save()
            if '_save' in request.POST:
                return redirect('ministrys')
            elif '_addanother' in request.POST:
                return redirect('upload_ministry')
            else:
                return redirect('edit_ministry')
    else:
        form = MinistrysForm(instance=ministry)
    data = {
        'title': f"Planning-{ministry.name}",
        'form': form
    }
    return render(request, 'ministrys/update/edit_ministry.html', data)

@permission_required('ministrys.can_delete', raise_exception=True)
def delete_ministry(request, ministry_id):
    ministry = get_object_or_404(Ministry, pk=ministry_id)
    ministry.delete()
    data = {
        'title': f"Planning-{ministry.name}",
        'ministry': ministry
    }
    return render(request, 'ministrys/update/deleted.html', data)