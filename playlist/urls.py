from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musics/', views.MusicListGeneric.as_view()),
    path('music/<int:pk>/', views.MusicDetailGeneric.as_view())
]
