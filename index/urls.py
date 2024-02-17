from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("songs/", views.songs, name="songs"),
    path("songs/search/", views.search_songs, name="search"),
    path('songs/<int:song_id>', views.song, name='song'),
    path('songs/add_song/', views.upload_song, name='upload_song'),
    path('songs/edit_song/<int:song_id>', views.edit_song, name='edit_song'),
    path('songs/delete_song/<int:song_id>', views.delete_song, name='delete_song'),

    path("ministrys/", views.ministrys, name="ministrys"),
    path('ministrys/<int:ministry_id>/', views.ministry, name='ministry'),
    path('ministrys/add_ministry/', views.upload_ministry, name='upload_ministry'),
    path('ministrys/edit_ministry/<int:ministry_id>/', views.edit_ministry, name='edit_ministry'),
    path('ministrys/delete_ministry/<int:ministry_id>', views.delete_ministry, name='delete_ministry'),
]