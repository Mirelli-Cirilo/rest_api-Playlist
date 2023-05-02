from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'musics', views.MusicViewSet)
router.register(r'music-detail', views.MusicDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
