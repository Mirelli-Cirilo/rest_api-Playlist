from rest_framework.serializers import ModelSerializer
from .models import Music
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password') 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        

class MusicSerializer(ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
