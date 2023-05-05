from .models import Music
from .serializers import MusicSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework import viewsets, mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters


class LoginViewSet(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            return Response({'Token:': user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserCreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class MusicViewSet(viewsets.ModelViewSet):
    
    serializer_class = MusicSerializer
    
    def get_queryset(self):       
        user = self.request.user
        return Music.objects.filter(user=user)

class MusicDetail(GenericViewSet, 
                mixins.ListModelMixin, 
                mixins.DestroyModelMixin, 
                mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin):
    
    serializer_class = MusicSerializer
    
    def get_queryset(self):       
        user = self.request.user
        return Music.objects.filter(user=user)
    
    