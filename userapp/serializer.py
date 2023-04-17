from rest_framework import serializers
from .models import *
class UserSerializer(serializers.Serializer):
    class Meta:
        model=User
        fields=['id','username','password']
class ProfilSerialzier(serializers.Serializer):
    class Meta:
        model=Profil
        fields="__all__"
class LoginUserSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

