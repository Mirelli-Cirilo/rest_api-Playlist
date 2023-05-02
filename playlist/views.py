from .models import Music
from .serializers import MusicSerializer

from rest_framework import viewsets, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicDetail(GenericViewSet, 
                mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer