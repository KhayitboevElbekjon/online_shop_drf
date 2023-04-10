from rest_framework import serializers
from asosiy.models import Bolim,Mahsulot,Izoh


class BolimSerializer(serializers.Serializer):
    class Meta:
        model=Bolim
        fields="__all__"
class MahsulotSerializer(serializers.Serializer):
    class Meta:
        model=Mahsulot
        fields="__all__"
class IzohSerializer(serializers.Serializer):
    class Meta:
        model=Izoh
        fields="__all__"