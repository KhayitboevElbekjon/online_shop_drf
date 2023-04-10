from rest_framework import serializers
from userapp.models import Profil
class ProfilSerialzier(serializers.Serializer):
    class Meta:
        model=Profil
        fields="__all__"

