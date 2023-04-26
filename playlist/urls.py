from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musics/', views.listMusics),
    path('music/<int:id>/', views.musicDetail)
]
