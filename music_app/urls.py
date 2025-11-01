from django.contrib import admin
from django.urls import path, include, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path('logout', logout, name="logout"),
    path('likesong', likesong, name = "likesong"),
    path('allSongs', allSongs, name="allSongs"),
    path('history', history, name="history"),
    path('song/<int:id>', songpost, name='songpost'),
    path('album/<int:id>', singerpost, name='singerpost'),
    path('createPlaylist', createPlaylist, name='createPlaylist'),
    path('myPlaylist/<int:id>', myPlaylist, name='myPlaylist'),
    path('addSongToPlaylist', addSongToPlaylist, name='addSongToPlaylist'),
    path('deletePlaylist', deletePlaylist, name='deletePlaylist'),
    path('searchResults', searchResults, name='searchResults'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
    path('accounts/', include('allauth.urls')),
    path('footer/',footer ,name="footer"),
    path('formex/',formex,name='formex'),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
