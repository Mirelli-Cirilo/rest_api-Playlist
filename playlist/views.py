from .models import Music
from .serializers import MusicSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class MusicListGeneric(ListCreateAPIView):
    queryset = Music.objects.all()   
    serializer_class = MusicSerializer

class MusicDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer